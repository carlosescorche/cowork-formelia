#!/usr/bin/env python3
"""
Formelia — Empaquetador de piezas HTML

Convierte una pieza de varios archivos en un HTML autocontenido: mete el CSS
dentro y sustituye las tipografías de Google Fonts por woff2 incrustados en
base64.

    python3 empaquetar.py ../assets/plantillas/motion-identidad/motion-identidad.html

Deja el resultado al lado, con sufijo `-completo.html`, y cachea las fuentes
en `fuentes.css` en la misma carpeta.

POR QUÉ HACE FALTA
Una pieza que se va a capturar en vídeo no puede depender de la red: si la
fuente llega tarde, los primeros fotogramas salen con la tipografía de
respaldo y luego cambia a mitad del vídeo. Incrustada, la pieza se renderiza
igual siempre y también funciona sin conexión o dentro de un visor que
bloquee peticiones externas.

Solo se incrustan los subconjuntos `latin` y `latin-ext`: son los que necesita
el español y evitan cargar cirílico o griego que nunca vamos a usar.
"""

import argparse
import base64
import pathlib
import re
import sys
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
SUBCONJUNTOS = ("latin", "latin-ext")


def bajar(url: str) -> bytes:
    return urllib.request.urlopen(
        urllib.request.Request(url, headers={"User-Agent": UA})).read()


def fuentes_incrustadas(url_google: str, cache: pathlib.Path) -> str:
    """Descarga una hoja de Google Fonts y devuelve sus @font-face con el
    woff2 en base64. Cachea el resultado para no volver a bajarlo."""
    if cache.exists():
        return cache.read_text(encoding="utf-8")

    hoja = bajar(url_google).decode("utf-8")
    bloques = []
    # Google precede cada @font-face de un comentario con el subconjunto.
    for subconjunto, cuerpo in re.findall(
            r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{[^}]*\})", hoja):
        if subconjunto not in SUBCONJUNTOS:
            continue
        url = re.search(r"url\((https://[^)]+\.woff2)\)", cuerpo).group(1)
        datos = base64.b64encode(bajar(url)).decode("ascii")
        cuerpo = cuerpo.replace(f"url({url}) format('woff2')",
                                f"url(data:font/woff2;base64,{datos}) format('woff2')")
        bloques.append(f"/* {subconjunto} */\n{cuerpo}")

    if not bloques:
        raise SystemExit(f"no se encontró ningún @font-face utilizable en {url_google}")
    css = "\n".join(bloques) + "\n"
    cache.write_text(css, encoding="utf-8")
    return css


def empaquetar(entrada: pathlib.Path, salida: pathlib.Path) -> None:
    html = entrada.read_text(encoding="utf-8")
    carpeta = entrada.parent

    enlaces = re.findall(r'<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"[^>]*>', html)
    locales = [h for h in enlaces if not h.startswith(("http://", "https://", "//"))]
    if not locales:
        raise SystemExit("la pieza no enlaza ninguna hoja de estilos local")

    for href in locales:
        ruta = carpeta / href
        if not ruta.exists():
            raise SystemExit(f"falta la hoja {ruta}")
        estilos = ruta.read_text(encoding="utf-8")

        incrustadas = ""
        for url in re.findall(r"@import\s+url\(['\"]?(https://fonts\.googleapis\.com[^'\")]+)",
                              estilos):
            incrustadas += fuentes_incrustadas(url, carpeta / "fuentes.css")
        estilos = re.sub(r"^@import url\([^)]*\);\s*$", "", estilos, flags=re.M)

        etiqueta = re.search(
            r'<link[^>]+rel="stylesheet"[^>]+href="' + re.escape(href) + r'"[^>]*>', html)
        html = html.replace(etiqueta.group(0), f"<style>\n{incrustadas}\n{estilos}</style>")

    salida.write_text(html, encoding="utf-8")
    print(f"{salida.name}: {salida.stat().st_size / 1024:.0f} kB")


def main() -> None:
    p = argparse.ArgumentParser(description="Empaqueta una pieza HTML en un solo archivo.")
    p.add_argument("pieza", type=pathlib.Path)
    p.add_argument("-o", "--salida", type=pathlib.Path)
    args = p.parse_args()

    if not args.pieza.exists():
        sys.exit(f"no existe {args.pieza}")
    salida = args.salida or args.pieza.with_name(args.pieza.stem + "-completo.html")
    empaquetar(args.pieza, salida)


if __name__ == "__main__":
    main()
