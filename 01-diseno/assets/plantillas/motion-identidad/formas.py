#!/usr/bin/env python3
"""
Formelia — Formas de partida del isotipo, morfables

Genera los paths que la apertura del motion usa como estado inicial de cada
capa del isotipo. Solo hace falta correrlo si cambia la marca o si se quiere
otra forma de partida; los valores que la pieza usa hoy ya están escritos en
`motion-identidad.css`.

    python3 formas.py        # imprime los paths para pegarlos en el CSS

CSS interpola la propiedad `d` entre dos paths solo si comparten estructura
de comandos (mismos M/L/C/Z en el mismo orden). Este script construye, para
cada capa del isotipo, formas de partida —cuadrado, rombo y rombo curvo—
expresadas con la estructura exacta del path de esa capa:

  1. Cada ancla del path original se coloca sobre el perímetro de la forma
     destino en la misma fracción de recorrido que ocupa en la capa, con el
     mismo sentido de giro. Así el morfado no se retuerce.
  2. Las cuatro anclas más cercanas a las esquinas se clavan en ellas: sin
     eso, ningún vértice cae en una esquina y la forma se lee achaflanada.
  3. Los puntos de control de cada tramo salen de subdividir (de Casteljau)
     la curva del lado correspondiente, así que los lados curvos del rombo
     curvo se reproducen de verdad, no por aproximación.

El isotipo son dos capas idénticas desplazadas (+24,66, +42,95) que se tocan
en una sola esquina, (82,7 · 102,1). Partir el path maestro por esa esquina
las separa sin alterar un solo punto de la marca.
"""

import math
import re

# Tamaños en unidades del lockup. La capa mide 49,8 x 85,7.
LADO_CUADRADO = 56.0      # lado completo
RADIO_ROMBO = 39.6        # media diagonal; misma área que el cuadrado
RADIO_ESTRELLA = 46.0     # más grande: los lados cóncavos le comen área
CONCAVIDAD = 0.38         # 0 = lados rectos, 1 = puntas totalmente colapsadas

CAPA_ABAJO = "M82.8667 102.023C94.0006 95.4006 105.354 89.0267 116.544 82.4951C121.819 79.4169 127.026 76.3914 132.442 73.5672C132.307 76.4916 132.417 80.2678 132.418 83.2566L132.425 101.92C130.038 103.665 127.552 104.928 124.994 106.388L113.1 113.221C111.607 114.093 109.193 115.418 107.846 116.402C107.634 119.3 107.75 122.857 107.726 125.797C107.676 132.107 107.802 138.448 107.714 144.758C105.862 146.066 103.408 147.387 101.413 148.526C96.7775 151.17 92.1219 153.855 87.4135 156.365C86.0155 157.109 84.3336 158.488 82.7523 159.383C82.5758 153.576 82.7088 147.055 82.7118 141.197L82.6909 102.227Z"

CAPA_ARRIBA = "M107.698 30.6169L107.812 30.8509C107.675 40.2984 107.917 49.9239 107.691 59.2893C106.448 60.139 104.187 61.3048 102.811 62.1296C98.4167 64.7645 93.8204 67.1672 89.4154 69.7954C87.3857 71.0064 84.6751 72.3486 82.8559 73.7545C82.7821 78.6788 82.7634 83.6038 82.8 88.5286C82.7747 93.0268 82.797 97.5253 82.8667 102.023L82.6909 102.227C80.8793 103.53 77.9597 104.892 75.9216 106.162C72.4835 108.303 68.7749 110.231 65.2667 112.283C62.8408 113.701 60.5651 115.15 58 116.301C58.2851 102.796 57.9973 89.1201 58.0998 75.6C58.1401 70.2881 57.9852 64.7394 58.154 59.4515C59.3718 58.3003 62.4617 56.6859 64.0091 55.8084L72.0602 51.194L99.9292 35.1389C102.529 33.6589 105.097 32.0463 107.698 30.6169Z"


# ---------- utilidades geométricas ----------

def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)


def dividir(bez, t):
    """Corta una cúbica en t y devuelve las dos mitades (de Casteljau)."""
    p0, p1, p2, p3 = bez
    a, b, c = lerp(p0, p1, t), lerp(p1, p2, t), lerp(p2, p3, t)
    d, e = lerp(a, b, t), lerp(b, c, t)
    f = lerp(d, e, t)
    return (p0, a, d, f), (f, e, c, p3)


def sub_bezier(bez, ta, tb):
    """Trozo de cúbica entre los parámetros ta y tb."""
    resto = bez if ta <= 1e-12 else dividir(bez, ta)[1]
    if 1.0 - ta <= 1e-12:
        return resto
    return dividir(resto, min((tb - ta) / (1.0 - ta), 1.0))[0]


def giro(pts):
    n = len(pts)
    return sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1]
               for i in range(n))


# ---------- lectura del path ----------

def parse(d):
    segmentos = []
    for cmd, resto in re.findall(r"([MLCZ])([^MLCZ]*)", d):
        nums = [float(x) for x in re.findall(r"-?\d+\.?\d*(?:e-?\d+)?", resto)]
        segmentos.append((cmd, nums))
    return segmentos


def anclas_de(segmentos):
    anclas = []
    for cmd, n in segmentos:
        if cmd in "ML":
            anclas.append((n[0], n[1]))
        elif cmd == "C":
            anclas.append((n[4], n[5]))
    return anclas


# ---------- forma destino ----------

def esquinas(tipo, cx, cy):
    if tipo == "cuadrado":
        h = LADO_CUADRADO / 2
        return [(cx + h, cy - h), (cx + h, cy + h), (cx - h, cy + h), (cx - h, cy - h)]
    r = RADIO_ROMBO if tipo == "rombo" else RADIO_ESTRELLA
    return [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]


def lados(tipo, ciclo, centro):
    """Las cuatro cúbicas del contorno, en orden."""
    salida = []
    for i in range(4):
        a, b = ciclo[i], ciclo[(i + 1) % 4]
        if tipo == "estrella":
            # Controles arrastrados hacia el centro: lados cóncavos.
            k = CONCAVIDAD
            c1 = lerp(a, centro, k)
            c2 = lerp(b, centro, k)
        else:
            c1, c2 = lerp(a, b, 1 / 3), lerp(a, b, 2 / 3)
        salida.append((a, c1, c2, b))
    return salida


def proyectar(ciclo, centro, p):
    """Distancia de perímetro (lados de longitud 1) donde el rayo
    centro→p corta el contorno del polígono.

    Rayo  C + s·D  contra lado  A + u·E, por la regla de Cramer:
      det = ex·dy − dx·ey ,  s = (ex·wy − ey·wx)/det ,  u = (dx·wy − dy·wx)/det
    con W = A − C. Vale la solución con s > 0 y u en [0, 1]."""
    cx, cy = centro
    dx, dy = p[0] - cx, p[1] - cy
    for i in range(4):
        a, b = ciclo[i], ciclo[(i + 1) % 4]
        ex, ey = b[0] - a[0], b[1] - a[1]
        det = ex * dy - dx * ey
        if abs(det) < 1e-12:
            continue
        wx, wy = a[0] - cx, a[1] - cy
        s = (ex * wy - ey * wx) / det
        u = (dx * wy - dy * wx) / det
        if s > 0 and -1e-9 <= u <= 1 + 1e-9:
            return i + min(max(u, 0.0), 1.0)
    raise AssertionError("el rayo no cortó el contorno")


def construir(d, tipo):
    segmentos = parse(d)
    anclas = anclas_de(segmentos)
    n = len(anclas)

    xs = [p[0] for p in anclas]
    ys = [p[1] for p in anclas]
    centro = ((min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2)

    # Fracción de perímetro de cada ancla, sobre la poligonal cerrada.
    tramos = [math.dist(anclas[i], anclas[(i + 1) % n]) for i in range(n)]
    total = sum(tramos)
    frac = [0.0]
    for i in range(n - 1):
        frac.append(frac[-1] + tramos[i] / total)

    ciclo = esquinas(tipo, *centro)
    if (giro(anclas) > 0) != (giro(ciclo) > 0):
        ciclo = list(reversed(ciclo))

    d0 = proyectar(ciclo, centro, anclas[0])
    dist = [d0 + f * 4.0 for f in frac]

    # Clavar en cada esquina el ancla más próxima.
    def circular(a, b):
        v = (a - b) % 4.0
        return min(v, 4.0 - v)

    usados = set()
    for k in range(4):
        objetivo = float(k)
        orden = sorted(range(n), key=lambda i: circular(dist[i], objetivo))
        i = next(j for j in orden if j not in usados)
        usados.add(i)
        vueltas = round((dist[i] - objetivo) / 4.0)
        dist[i] = objetivo + vueltas * 4.0
    assert len(usados) == 4, "dos esquinas se pelearon por el mismo vértice"
    assert all(dist[i] < dist[i + 1] + 1e-9 for i in range(n - 1)), \
        "el clavado rompió el orden de las anclas"

    curvas_lado = lados(tipo, ciclo, centro)

    def punto(dis):
        e = int(math.floor(dis + 1e-9)) % 4
        t = dis - math.floor(dis + 1e-9)
        return dividir(curvas_lado[e], t)[0][3] if t > 1e-12 else curvas_lado[e][0]

    puntos = [punto(v) for v in dist]

    # Tramo que une cada ancla con la siguiente, dentro de su mismo lado.
    curvas = []
    for i in range(n):
        da = dist[i]
        db = dist[i + 1] if i + 1 < n else dist[0] + 4.0
        base = math.floor(da + 1e-9)
        ta, tb = da - base, db - base
        assert tb <= 1.0 + 1e-6, "un tramo cruza una esquina"
        curvas.append(sub_bezier(curvas_lado[int(base) % 4], ta, min(tb, 1.0)))

    def f2(v):
        return f"{v:.2f}"

    salida, j = [], 0
    for cmd, _ in segmentos:
        if cmd == "M":
            p = puntos[0]
            salida.append(f"M{f2(p[0])} {f2(p[1])}")
        elif cmd == "L":
            j += 1
            p = puntos[j]
            salida.append(f"L{f2(p[0])} {f2(p[1])}")
        elif cmd == "C":
            j += 1
            p, bz = puntos[j], curvas[j - 1]
            salida.append(f"C{f2(bz[1][0])} {f2(bz[1][1])} "
                          f"{f2(bz[2][0])} {f2(bz[2][1])} {f2(p[0])} {f2(p[1])}")
        elif cmd == "Z":
            salida.append("Z")
    return "".join(salida)


def main():
    piezas = [
        ("capa de abajo · rombo curvo", "estrella", CAPA_ABAJO),
        ("capa de abajo · rombo recto", "rombo", CAPA_ABAJO),
        ("capa de arriba · rombo curvo", "estrella", CAPA_ARRIBA),
        ("capa de arriba · rombo recto", "rombo", CAPA_ARRIBA),
    ]
    print("Pegar en los @keyframes capa-abajo / capa-arriba de motion-identidad.css.\n"
          f"Parámetros: rombo r {RADIO_ROMBO} · rombo curvo r {RADIO_ESTRELLA}, "
          f"concavidad {CONCAVIDAD}\n")
    for titulo, tipo, d in piezas:
        print(f"/* {titulo} */")
        print(construir(d, tipo))
        print()


if __name__ == "__main__":
    main()
