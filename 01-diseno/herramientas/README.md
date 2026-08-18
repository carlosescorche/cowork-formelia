# Herramientas de diseño

> Última actualización: 2026-08-12

Utilidades para producir piezas animadas en HTML/CSS y sacarlas a vídeo. No son assets:
son el instrumental con el que se fabrican. Sirven para cualquier pieza, no solo para la
que las estrenó.

Requisitos: Python 3 (el del sistema basta, no hace falta instalar nada), `ffmpeg` en el
PATH y Google Chrome.

| Herramienta | Qué hace |
| --- | --- |
| [`empaquetar.py`](empaquetar.py) | Convierte una pieza de varios archivos en un HTML autocontenido |
| [`exportar-video.py`](exportar-video.py) | Graba una pieza animada a MP4, fotograma a fotograma |
| [`capturar-ui.py`](capturar-ui.py) | Captura pantallas reales de la app siguiendo un plan JSON |

## empaquetar.py

Mete el CSS dentro del HTML y sustituye las tipografías de Google Fonts por woff2
incrustados en base64 (subconjuntos `latin` y `latin-ext`, que es lo que necesita el
español).

```bash
python3 empaquetar.py ../assets/plantillas/motion-identidad/motion-identidad.html
```

Deja el resultado al lado con sufijo `-completo.html` y cachea las fuentes en `fuentes.css`.
Ninguno de los dos se versiona: se regeneran.

**Por qué hace falta.** Una pieza que se va a grabar no puede depender de la red: si la
tipografía llega tarde, los primeros fotogramas salen con la de respaldo y luego cambia a
mitad del vídeo. Incrustada, la pieza se renderiza igual siempre, funciona sin conexión y
sobrevive a un visor que bloquee peticiones externas.

## exportar-video.py

Graba la pieza a MP4 sin depender del reloj real.

```bash
python3 exportar-video.py pieza-completo.html \
  --tamano 1080x1920 --params "solo=crema&formato=9x16" \
  --salida ../../assets/pieza/pieza-9x16.mp4 --fps 30
```

Salida H.264 High, yuv420p, CRF 18, `+faststart`: lo que piden Instagram y TikTok.

### Transparencia

Con `--alfa` conserva el canal alfa. La extensión de `--salida` decide el códec:

| Extensión | Códec | Para qué |
| --- | --- | --- |
| `.mov` | ProRes 4444 (`yuva444p10le`) | Editar. Pesa, pero lo abre cualquier programa |
| `.webp` | WebP animado (libwebp) | Web y navegador. Unas treinta veces más ligero |

`.mp4` con `--alfa` da error a propósito: **H.264 no tiene canal alfa**, no es una
limitación del script. Y ojo, la transparencia no sirve para publicar en Instagram ni
TikTok: ambos la aplanan. Es para componer.

**`.webm` también da error, y por una razón que conviene saber:** ffmpeg 7.1 acepta
`-pix_fmt yuva420p` con `libvpx-vp9`, no protesta, y escribe `yuv420p`. El alfa se pierde
en silencio. Comprobado extrayendo el canal del archivo resultante.

Dos condiciones que hay que cumplir a la vez, o el alfa sale opaco sin avisar:

- El script pone `Emulation.setDefaultBackgroundColorOverride` en transparente; sin eso
  Chrome compone sobre blanco.
- **La pieza no puede pintar fondo en modo `limpio`.** Es el error fácil: dejar un tablero
  de cuadros para ver la transparencia en la vista previa y que acabe grabado en el vídeo.
  El tablero va en la vista normal; en `limpio` el body no pinta nada.

Para comprobar que el alfa es real y no solo un canal presente pero opaco:

```bash
ffmpeg -i salida.mov -vf "alphaextract,format=gray" -frames:v 1 alfa.png
```

Si el canal sale todo a 255, es opaco. Elegir un fotograma **con contenido**: al principio
del ciclo la escena está vacía y un alfa todo a cero es correcto, no un fallo.

El WebP animado no se puede verificar así — el decodificador de ffmpeg solo lee WebP fijo.
Se comprueba leyendo el contenedor: el chunk `VP8X` lleva un byte de flags con el bit
`0x10` (alfa) y el `0x02` (animación), y los chunks `ANMF` son los fotogramas. Ojo, libwebp
deduplica fotogramas iguales, así que salen menos de los capturados; lo que hay que
comprobar es que la **suma de duraciones** siga dando el ciclo completo.

### Contrato que debe cumplir la pieza

1. Exponer `window.congelar(ms)`: pausa todas las animaciones y las coloca en ese
   milisegundo del ciclo.
2. Marcar `document.body.dataset.listo = '1'` cuando ya pueda capturarse, normalmente
   tras `document.fonts.ready`.
3. Exponer `window.DURACION_MS`, o pasar la duración con `--duracion`.

Además debe aceptar `?limpio=1` (sin cabecera ni controles) y `?zoom=1` (tamaño real).
Una pieza construida sobre un único reloj CSS cumple todo esto de serie.

### Por qué está hecho así

- **Chrome con `--screenshot` tarda unos 3,7 s por lanzamiento.** Un vídeo de 500
  fotogramas serían más de media hora. Aquí se lanza Chrome una sola vez y se le habla por
  CDP, el protocolo de DevTools: baja a menos de dos minutos.
- **No usar `--virtual-time-budget`.** No adelanta el reloj de las animaciones CSS y
  devuelve fotogramas congelados y falsos. Es la trampa evidente y no funciona.
- **Fijar el reloj en vez de grabar en tiempo real** hace la captura determinista: dos
  ejecuciones dan exactamente los mismos píxeles.
- **Python del sistema no trae cliente WebSocket.** En vez de instalar dependencias en la
  máquina del founder, el script lleva dentro el mínimo imprescindible (handshake y
  tramas). Son unas ochenta líneas y no se tocan.

## capturar-ui.py

Abre Chrome por CDP, ejecuta un plan JSON de pasos (navegar, esperar, escribir, clic,
capturar) y deja las capturas PNG en disco. Es la fuente de "UI siempre real" de las piezas
de video: cuando la UI cambia, se reejecuta el plan y las capturas se regeneran con el
mismo encuadre.

```bash
python3 capturar-ui.py plan-captura.json --salida capturas/
```

Las credenciales nunca van en el plan: el plan usa `${VARIABLES}` y el script las
sustituye desde el `.env` de la raíz del repo (que está en `.gitignore`). Con `--ver`
ejecuta con Chrome visible, para depurar un plan que falla. Los verbos y un ejemplo
completo con login están documentados en el skill `pantallas-reel`
(`.claude/skills/pantallas-reel/references/plan-captura.md`), que es quien lo usa.

## Cómo construir una pieza que funcione con esto

Lo que hace que todo encaje es una sola regla: **un único reloj**. Cada animación dura lo
mismo que el ciclo completo, es `infinite` y coloca su tramo con porcentajes; ninguna usa
`animation-delay` para secuenciar.

De ahí salen tres propiedades que valen la pena:

- La pieza se reproduce y se repite **sin JavaScript**, así que funciona en cualquier visor.
- Todo queda en fase entre ciclos, sin desfases acumulados.
- Cualquier instante se puede congelar, que es justo lo que el exportador necesita.

Dos avisos que cuestan una tarde si se descubren tarde:

- Dentro de `@keyframes`, `animation-timing-function` **no admite `var()`**: Chrome la
  descarta y el tramo cae a la curva del atajo. Hay que escribir la cúbica literal.
- La propiedad `d` solo se anima sobre un `<path>` real, **nunca sobre un `<use>`**. Y solo
  interpola si los dos paths comparten estructura de comandos.
