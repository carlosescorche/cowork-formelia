#!/usr/bin/env python3
"""
Formelia — Captura de UI real por plan de pasos

Abre Chrome, ejecuta un plan JSON (navegar, esperar, escribir, clic, capturar)
y deja las capturas PNG en disco. Es la fuente de "UI siempre real" para las
piezas de video: cada fotograma clave de una animacion sale de aqui.

    python3 capturar-ui.py plan-captura.json --salida capturas/

Las credenciales NUNCA van en el plan: el plan usa ${VARIABLES} y este script
las sustituye desde un archivo .env (por defecto el de la raiz del repo, que
esta en .gitignore).

PLAN DE EJEMPLO
    {
      "url": "${FORMELIA_APP_URL}",
      "viewport": {"ancho": 390, "alto": 844, "escala": 3, "movil": true},
      "pasos": [
        {"ir": "/es/login"},
        {"esperar": "input[type=email]"},
        {"escribir": ["input[type=email]", "${FORMELIA_DEMO_EMAIL}"]},
        {"escribir": ["input[type=password]", "${FORMELIA_DEMO_PASSWORD}"]},
        {"clic": "button[type=submit]"},
        {"esperar_url": "dashboard"},
        {"captura": "01-dashboard"}
      ]
    }

VERBOS: ver el README de esta carpeta o references/plan-captura.md del skill
pantallas-reel.

POR QUE ASI
  - Un plan versionable hace la captura repetible: cuando la UI cambie, se
    reejecuta el plan y las capturas se regeneran identicas en encuadre.
  - Chrome se lanza una vez y se maneja por CDP (protocolo de DevTools),
    igual que exportar-video.py, sin instalar dependencias.
  - `escribir` usa Input.insertText, que dispara los eventos que un React
    controlado necesita; `clic` manda eventos de raton reales al centro del
    elemento, no element.click().
"""

import argparse
import base64
import json
import os
import pathlib
import re
import socket
import struct
import subprocess
import sys
import time
import urllib.request

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

UA_MOVIL = ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 "
            "Mobile/15E148 Safari/604.1")


# ---------------------------------------------------------------- WebSocket
# (identico al de exportar-video.py: minimo imprescindible para CDP)

class WebSocket:
    def __init__(self, url):
        resto = url[len("ws://"):]
        hostport, _, ruta = resto.partition("/")
        host, _, puerto = hostport.partition(":")
        self.sock = socket.create_connection((host, int(puerto)))
        self.sock.settimeout(60)
        clave = base64.b64encode(os.urandom(16)).decode()
        self.sock.sendall((
            f"GET /{ruta} HTTP/1.1\r\n"
            f"Host: {hostport}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {clave}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        ).encode())
        self.buf = b""
        while b"\r\n\r\n" not in self.buf:
            self.buf += self.sock.recv(65536)
        cabeceras, _, self.buf = self.buf.partition(b"\r\n\r\n")
        if b"101" not in cabeceras.split(b"\r\n")[0]:
            raise RuntimeError(f"el servidor no acepto el upgrade: {cabeceras[:120]}")

    def _leer(self, n):
        while len(self.buf) < n:
            trozo = self.sock.recv(1 << 20)
            if not trozo:
                raise ConnectionError("Chrome cerro la conexion")
            self.buf += trozo
        salida, self.buf = self.buf[:n], self.buf[n:]
        return salida

    def enviar(self, texto):
        datos = texto.encode()
        n = len(datos)
        cabecera = bytearray([0x81])
        if n < 126:
            cabecera.append(0x80 | n)
        elif n < 65536:
            cabecera.append(0x80 | 126)
            cabecera += struct.pack(">H", n)
        else:
            cabecera.append(0x80 | 127)
            cabecera += struct.pack(">Q", n)
        mascara = os.urandom(4)
        cabecera += mascara
        self.sock.sendall(bytes(cabecera) +
                          bytes(b ^ mascara[i % 4] for i, b in enumerate(datos)))

    def recibir(self):
        trozos = []
        while True:
            b0, b1 = self._leer(2)
            fin, opcode = bool(b0 & 0x80), b0 & 0x0F
            n = b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._leer(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._leer(8))[0]
            carga = self._leer(n)
            if opcode == 0x8:
                raise ConnectionError("Chrome cerro la sesion")
            if opcode == 0x9:
                self.sock.sendall(b"\x8a\x80" + os.urandom(4))
                continue
            trozos.append(carga)
            if fin:
                return b"".join(trozos).decode()


class CDP:
    def __init__(self, ws):
        self.ws, self.n = ws, 0

    def __call__(self, metodo, **params):
        self.n += 1
        self.ws.enviar(json.dumps({"id": self.n, "method": metodo, "params": params}))
        while True:
            msg = json.loads(self.ws.recibir())
            if msg.get("id") != self.n:
                continue
            if "error" in msg:
                raise RuntimeError(f"{metodo}: {msg['error']}")
            return msg.get("result", {})

    def evaluar(self, expresion):
        r = self("Runtime.evaluate", expression=expresion, returnByValue=True)
        if "exceptionDetails" in r:
            raise RuntimeError(f"JS fallo: {r['exceptionDetails'].get('text')}")
        return r.get("result", {}).get("value")


def puerto_libre():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def abrir_chrome(ver=False):
    puerto = puerto_libre()
    argumentos = [CHROME, f"--remote-debugging-port={puerto}",
                  "--no-first-run", "--no-default-browser-check",
                  "--hide-scrollbars", "--user-data-dir=" +
                  str(pathlib.Path.home() / ".cache" / "formelia-capturas"),
                  "about:blank"]
    if not ver:
        argumentos.insert(1, "--headless=new")
        argumentos.insert(2, "--disable-gpu")
    proc = subprocess.Popen(argumentos, stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
    limite = time.time() + 30
    while time.time() < limite:
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{puerto}/json", timeout=1) as r:
                for t in json.load(r):
                    if t.get("type") == "page" and t.get("webSocketDebuggerUrl"):
                        return proc, CDP(WebSocket(t["webSocketDebuggerUrl"]))
        except Exception:
            time.sleep(0.25)
    proc.kill()
    raise RuntimeError("Chrome no levanto el puerto de depuracion")


# ---------------------------------------------------------------- entorno

def cargar_env(ruta):
    valores = {}
    for linea in ruta.read_text().splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        clave, _, valor = linea.partition("=")
        valores[clave.strip()] = valor.strip()
    return valores


def sustituir(texto, entorno):
    def reemplazo(m):
        nombre = m.group(1)
        if nombre not in entorno:
            sys.exit(f"la variable ${{{nombre}}} del plan no esta en el .env")
        return entorno[nombre]
    return re.sub(r"\$\{([A-Z0-9_]+)\}", reemplazo, texto)


# ---------------------------------------------------------------- pasos

def esperar_selector(cdp, selector, timeout=15):
    sel = json.dumps(selector)
    limite = time.time() + timeout
    while time.time() < limite:
        visible = cdp.evaluar(
            f"(() => {{ const e = document.querySelector({sel});"
            f" if (!e) return false; const r = e.getBoundingClientRect();"
            f" return r.width > 0 && r.height > 0; }})()")
        if visible:
            return
        time.sleep(0.2)
    raise RuntimeError(f"no aparecio el selector {selector} en {timeout}s")


def centro(cdp, selector):
    sel = json.dumps(selector)
    caja = cdp.evaluar(
        f"(() => {{ const e = document.querySelector({sel});"
        f" if (!e) return null; e.scrollIntoView({{block:'center'}});"
        f" const r = e.getBoundingClientRect();"
        f" return [r.left + r.width/2, r.top + r.height/2]; }})()")
    if not caja:
        raise RuntimeError(f"no existe el selector {selector}")
    return caja


def clic(cdp, selector):
    x, y = centro(cdp, selector)
    for tipo, cuenta in [("mousePressed", 1), ("mouseReleased", 1)]:
        cdp("Input.dispatchMouseEvent", type=tipo, x=x, y=y,
            button="left", clickCount=cuenta)


def escribir(cdp, selector, texto):
    esperar_selector(cdp, selector)
    clic(cdp, selector)                       # foco con evento real
    cdp("Input.insertText", text=texto)       # dispara input como un pegado


def aplicar_viewport(cdp, vp):
    cdp("Emulation.setDeviceMetricsOverride",
        width=vp.get("ancho", 390), height=vp.get("alto", 844),
        deviceScaleFactor=vp.get("escala", 3), mobile=vp.get("movil", True))
    if vp.get("movil", True):
        cdp("Emulation.setUserAgentOverride", userAgent=UA_MOVIL)


def ejecutar(plan, salida, entorno, ver=False):
    base = sustituir(plan.get("url", "${FORMELIA_APP_URL}"), entorno).rstrip("/")
    salida.mkdir(parents=True, exist_ok=True)
    proc, cdp = abrir_chrome(ver)
    capturadas = []
    try:
        cdp("Page.enable")
        aplicar_viewport(cdp, plan.get("viewport", {}))

        for i, paso in enumerate(plan["pasos"], 1):
            (verbo, arg), = paso.items()
            if isinstance(arg, str):
                arg = sustituir(arg, entorno)
            elif isinstance(arg, list):
                arg = [sustituir(a, entorno) if isinstance(a, str) else a for a in arg]
            etiqueta = arg if verbo != "escribir" else [arg[0], "***"]
            print(f"  {i:2d}. {verbo} {etiqueta}")

            if verbo == "ir":
                destino = arg if "://" in arg else base + arg
                cdp("Page.navigate", url=destino)
                limite = time.time() + 30
                while cdp.evaluar("document.readyState") != "complete":
                    if time.time() > limite:
                        raise RuntimeError(f"paso {i}: la pagina no termino de cargar")
                    time.sleep(0.2)
            elif verbo == "esperar":
                esperar_selector(cdp, arg)
            elif verbo == "esperar_url":
                limite = time.time() + 30
                while arg not in cdp.evaluar("location.href"):
                    if time.time() > limite:
                        raise RuntimeError(f"paso {i}: la URL nunca contuvo '{arg}' "
                                           f"(esta en {cdp.evaluar('location.href')})")
                    time.sleep(0.2)
            elif verbo == "pausa":
                time.sleep(arg / 1000)
            elif verbo == "clic":
                esperar_selector(cdp, arg)
                clic(cdp, arg)
            elif verbo == "escribir":
                escribir(cdp, arg[0], arg[1])
            elif verbo == "tecla":
                for tipo in ("keyDown", "keyUp"):
                    cdp("Input.dispatchKeyEvent", type=tipo, key=arg,
                        code=arg, windowsVirtualKeyCode=13 if arg == "Enter" else 0)
            elif verbo == "desplazar":
                cdp.evaluar(f"window.scrollBy(0, {int(arg)})")
                time.sleep(0.3)
            elif verbo == "viewport":
                aplicar_viewport(cdp, arg)
                time.sleep(0.3)
            elif verbo == "evaluar":
                cdp.evaluar(arg)
            elif verbo == "captura":
                time.sleep(0.4)               # deja asentar la ultima accion
                datos = cdp("Page.captureScreenshot", format="png",
                            fromSurface=True)["data"]
                destino = salida / f"{arg}.png"
                destino.write_bytes(base64.b64decode(datos))
                capturadas.append(destino)
                print(f"      -> {destino}")
            else:
                raise RuntimeError(f"paso {i}: verbo desconocido '{verbo}'")
    finally:
        proc.kill()
    return capturadas


def main():
    p = argparse.ArgumentParser(description="Captura UI real siguiendo un plan JSON.")
    p.add_argument("plan", type=pathlib.Path)
    p.add_argument("--salida", type=pathlib.Path, default=pathlib.Path("capturas"))
    p.add_argument("--env", type=pathlib.Path,
                   help="archivo .env; por defecto el de la raiz del repo")
    p.add_argument("--ver", action="store_true",
                   help="Chrome visible, para depurar un plan que falla")
    args = p.parse_args()

    if not args.plan.exists():
        sys.exit(f"no existe {args.plan}")
    if not pathlib.Path(CHROME).exists():
        sys.exit(f"no encuentro Chrome en {CHROME}")

    ruta_env = args.env or pathlib.Path(__file__).resolve().parents[2] / ".env"
    if not ruta_env.exists():
        sys.exit(f"no existe {ruta_env} — crea el .env con FORMELIA_APP_URL, "
                 "FORMELIA_DEMO_EMAIL y FORMELIA_DEMO_PASSWORD")
    entorno = {**cargar_env(ruta_env), **os.environ}

    plan = json.loads(args.plan.read_text())
    capturadas = ejecutar(plan, args.salida, entorno, args.ver)
    print(f"  {len(capturadas)} capturas en {args.salida}/")


if __name__ == "__main__":
    main()
