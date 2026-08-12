#!/usr/bin/env python3
"""
Formelia — Exportador de piezas animadas a MP4

Graba una animación HTML/CSS a vídeo, fotograma a fotograma y sin depender
del reloj real.

    python3 exportar-video.py pieza-completo.html --tamano 1080x1920 \
        --params "solo=crema&formato=9x16" --salida video/pieza-9x16.mp4

CONTRATO QUE DEBE CUMPLIR LA PIEZA
  1. Exponer `window.congelar(ms)`: pausa todas las animaciones y las coloca
     en ese milisegundo del ciclo.
  2. Marcar `document.body.dataset.listo = '1'` cuando ya pueda capturarse
     (normalmente tras `document.fonts.ready`).
  3. Exponer `window.DURACION_MS` con la duración del ciclo, o pasarla aquí
     con `--duracion`.
Las piezas construidas sobre un único reloj CSS lo cumplen de serie.

POR QUÉ ASÍ Y NO MÁS FÁCIL
  - Chrome headless con `--screenshot` tarda ~3,7 s por lanzamiento: 495
    fotogramas serían más de media hora por vídeo. Aquí se lanza Chrome UNA
    vez y se le habla por CDP (protocolo de DevTools).
  - NO usar `--virtual-time-budget`: no adelanta el reloj de las animaciones
    CSS y devuelve fotogramas congelados y falsos.
  - Al fijar el reloj por CDP en vez de grabar en tiempo real, la captura es
    determinista: dos ejecuciones dan exactamente los mismos píxeles.
  - Python del sistema no trae cliente WebSocket. En vez de instalar
    dependencias en la máquina, abajo va el mínimo imprescindible.
"""

import argparse
import base64
import json
import os
import pathlib
import shutil
import socket
import struct
import subprocess
import sys
import time
import urllib.request

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


# ---------------------------------------------------------------- WebSocket

class WebSocket:
    """Cliente mínimo, solo lo que CDP necesita: texto, sin extensiones."""

    def __init__(self, url):
        resto = url[len("ws://"):]
        hostport, _, ruta = resto.partition("/")
        host, _, puerto = hostport.partition(":")
        self.sock = socket.create_connection((host, int(puerto)))
        self.sock.settimeout(30)
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
            raise RuntimeError(f"el servidor no aceptó el upgrade: {cabeceras[:120]}")

    def _leer(self, n):
        while len(self.buf) < n:
            trozo = self.sock.recv(1 << 20)
            if not trozo:
                raise ConnectionError("Chrome cerró la conexión")
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
        mascara = os.urandom(4)          # el cliente siempre enmascara
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
            carga = self._leer(n)        # el servidor nunca enmascara
            if opcode == 0x8:
                raise ConnectionError("Chrome cerró la sesión")
            if opcode == 0x9:            # ping → pong
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
                continue                  # evento suelto, no interesa
            if "error" in msg:
                raise RuntimeError(f"{metodo}: {msg['error']}")
            return msg.get("result", {})

    def evaluar(self, expresion):
        r = self("Runtime.evaluate", expression=expresion, returnByValue=True)
        if "exceptionDetails" in r:
            raise RuntimeError(f"JS falló: {r['exceptionDetails'].get('text')}")
        return r.get("result", {}).get("value")


# ---------------------------------------------------------------- Chrome

def puerto_libre():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def abrir_chrome(url, ancho, alto):
    puerto = puerto_libre()
    proc = subprocess.Popen(
        [CHROME, "--headless=new", f"--remote-debugging-port={puerto}",
         "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
         "--no-first-run", "--no-default-browser-check",
         f"--window-size={ancho},{alto}", url],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

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
    raise RuntimeError("Chrome no levantó el puerto de depuración")


# ---------------------------------------------------------------- captura

def capturar(pieza, params, ancho, alto, fps, duracion, destino, alfa=False):
    url = pieza.as_uri() + "?limpio=1&zoom=1&t=0" + (f"&{params}" if params else "")
    proc, cdp = abrir_chrome(url, ancho, alto)
    try:
        cdp("Page.enable")
        cdp("Emulation.setDeviceMetricsOverride",
            width=ancho, height=alto, deviceScaleFactor=1, mobile=False)
        if alfa:
            # Sin esto Chrome compone sobre blanco opaco y el PNG sale sin alfa.
            cdp("Emulation.setDefaultBackgroundColorOverride",
                color={"r": 0, "g": 0, "b": 0, "a": 0})

        limite = time.time() + 30
        while cdp.evaluar("document.body.dataset.listo") != "1":
            if time.time() > limite:
                raise RuntimeError("la pieza nunca marcó body.dataset.listo — "
                                   "revisa que exponga congelar() y acepte ?t=")
            time.sleep(0.1)

        if duracion is None:
            duracion = cdp.evaluar("window.DURACION_MS")
            if not duracion:
                raise RuntimeError("la pieza no expone window.DURACION_MS: "
                                   "pásala con --duracion")

        total = round(duracion / 1000 * fps)
        for i in range(total):
            cdp.evaluar(f"congelar({i * duracion / total:.4f})")
            datos = cdp("Page.captureScreenshot", format="png",
                        fromSurface=True, captureBeyondViewport=False)["data"]
            (destino / f"f{i:05d}.png").write_bytes(base64.b64decode(datos))
            if i % 60 == 0 or i == total - 1:
                print(f"    {i + 1}/{total}", end="\r", flush=True)
        print(f"    {total}/{total} fotogramas · {duracion / 1000:.1f} s")
        return total
    finally:
        proc.kill()


def codificar(origen, fps, salida, alfa=False):
    """H.264 para publicar; ProRes 4444 o VP9 cuando hay que conservar el alfa.
    MP4/H.264 no tiene canal alfa: no hay forma de guardarlo ahí."""
    salida.parent.mkdir(parents=True, exist_ok=True)
    ext = salida.suffix.lower()

    if alfa and ext == ".mov":          # el estándar para editar
        codec = ["-c:v", "prores_ks", "-profile:v", "4444",
                 "-pix_fmt", "yuva444p10le", "-alpha_bits", "16"]
    elif alfa and ext == ".webp":       # para web
        codec = ["-c:v", "libwebp_anim", "-pix_fmt", "bgra",
                 "-lossless", "0", "-q:v", "82", "-loop", "0"]
    elif alfa and ext == ".webm":
        # ffmpeg 7.1 acepta `-pix_fmt yuva420p` con libvpx-vp9, no protesta y
        # escribe yuv420p: el alfa se pierde en silencio. Comprobado.
        raise SystemExit("VP9/WebM pierde el alfa en ffmpeg 7.1 sin avisar. "
                         "Usa .mov (ProRes 4444) para editar o .webp para web.")
    elif alfa:
        raise SystemExit("con --alfa la salida debe ser .mov (ProRes 4444) "
                         "o .webp (WebP animado). MP4/H.264 no admite alfa.")
    else:
        codec = ["-c:v", "libx264", "-profile:v", "high", "-preset", "slow",
                 "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart"]

    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps),
         "-i", str(origen / "f%05d.png"), *codec, str(salida)], check=True)


def main():
    p = argparse.ArgumentParser(description="Graba una pieza animada HTML a MP4.")
    p.add_argument("pieza", type=pathlib.Path, help="HTML autocontenido (ver empaquetar.py)")
    p.add_argument("--salida", type=pathlib.Path, required=True, help="ruta del .mp4")
    p.add_argument("--tamano", default="1080x1440", help="ANCHOxALTO, por defecto 1080x1440")
    p.add_argument("--params", default="", help="query extra para la pieza, p. ej. solo=crema")
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--duracion", type=int, help="ms del ciclo; por defecto window.DURACION_MS")
    p.add_argument("--alfa", action="store_true",
                   help="conserva la transparencia; la salida debe ser .mov o .webm")
    args = p.parse_args()

    if not args.pieza.exists():
        sys.exit(f"no existe {args.pieza}")
    if not pathlib.Path(CHROME).exists():
        sys.exit(f"no encuentro Chrome en {CHROME}")
    if not shutil.which("ffmpeg"):
        sys.exit("hace falta ffmpeg en el PATH")

    ancho, _, alto = args.tamano.partition("x")
    temporal = args.salida.parent / f".fotogramas-{args.salida.stem}"
    if temporal.exists():
        shutil.rmtree(temporal)
    temporal.mkdir(parents=True)

    print(f"  {args.salida.name}  ({args.tamano}, {args.fps} fps)")
    try:
        capturar(args.pieza.resolve(), args.params, int(ancho), int(alto),
                 args.fps, args.duracion, temporal, args.alfa)
        codificar(temporal, args.fps, args.salida, args.alfa)
    finally:
        shutil.rmtree(temporal, ignore_errors=True)
    print(f"    {args.salida.stat().st_size / 1e6:.1f} MB → {args.salida}")


if __name__ == "__main__":
    main()
