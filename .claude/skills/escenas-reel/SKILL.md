---
name: escenas-reel
description: Activa el sistema de escenas animadas para reels de Formelia — pantallas 1080×1920 en HTML/CSS/JS puro con controles de reproducción por escena, y exportación a MP4 fotograma a fotograma. Úsalo cuando el usuario pida animar escenas o pantallas para un reel o video vertical, simular la app de Formelia o un formulario genérico en movimiento, generar clips de producto para Instagram/TikTok, o diga "genera los clips de", "anima la escena de", "simula la pantalla de", "exporta los videos del reel" o similar. Actívalo también si un brief de video pide capturas animadas que no se pueden grabar de la app real.
---

# Escenas animadas para reels

Construyes escenas de video vertical (1080×1920, 9:16) como animaciones HTML/CSS/JS
puras dentro de un visor con controles, las iteras con el founder en el chat, y solo
tras su aprobación las exportas a MP4 con las herramientas del repo. El sistema completo
(arquitectura, contrato de captura, trampas de Chrome) está en
[references/sistema.md](references/sistema.md) — léelo antes de escribir código.
La plantilla base del visor está en [assets/plantilla.html](assets/plantilla.html):
empieza desde ella, no desde cero.

## Al activarte, SIEMPRE en este orden

1. **Pide el brief si no te lo dieron.** Los briefs de reels viven en
   `02-marketing/redes/instagram/<fecha>-<slug>/brief.md`. La tabla de producción del
   brief define qué se ve, el ritmo y la duración de cada escena — la animación se diseña
   desde ahí, no desde la imaginación.
2. **Reúne referencias visuales antes de diseñar.** Para pantallas de Formelia pide al
   founder capturas de pantalla o una URL pública (un formulario publicado no requiere
   login). La fuente definitiva del diseño es el código real en `../formelia-app`
   (`src/app/(app)/app.css`, `src/app/(respondent)/respondent.css`, componentes en
   `src/components/`, copy en `src/messages/es/`): tokens, radios, sombras y textos se
   copian literales de ahí, nunca se inventan. **No puedes autenticarte con contraseñas**
   aunque te las den: si hace falta ver una pantalla con login, pide capturas o que el
   founder navegue él mismo en el panel.
3. **Lee `00-core/marca/identidad-visual.md`** si la pieza usa la marca. Las escenas de
   "dolor" (formularios genéricos del problema) van sin marca Formelia a propósito:
   escala de grises, tipografía de sistema. El rojo de resaltado de dolor es el de error
   de UI, sobrio.

## Arquitectura del visor

Un solo HTML: una tarjeta por escena, cada una con su lienzo 1080×1920 escalado, botones
**Reproducir / Pausar / Reiniciar** y barra de progreso propios. Todas las animaciones
son CSS pausadas por defecto con una variable (`--ps`) que el controlador activa
forzando un recálculo síncrono — sin ese recálculo Chrome aplica el cambio tarde y
desincroniza los delays. El detalle exacto (y por qué cada pieza es como es) está en
`references/sistema.md`.

## Reglas de construcción

- **HTML, CSS y JS puros, sin librerías.** Las animaciones son keyframes CSS; el JS solo
  monta contenido (clones, tipeo por caracteres, filas generadas) y controla
  reproducción. Si una animación parece necesitar una librería, casi siempre es señal de
  que hay que simplificar la escena.
- **Fidelidad por código, no por ojo.** Pantallas de Formelia se replican leyendo los
  componentes reales: mismo copy, mismos hex, mismas transiciones (busca la duración y el
  easing en el código del producto y cópialos).
- **Nada de iconos ni emoji propios.** La iconografía funcional de la UI replicada sí va
  (flechas, banderas de país, spinners): es producto, no decoración nuestra.
- **Duraciones al brief.** Cada escena declara su duración en `data-dur` (segundos); las
  líneas de tiempo largas se orquestan con un solo reloj por elemento cuando hay estados
  que van y vuelven (ver la trampa de los fill en la referencia).

## Flujo de trabajo

1. **Animación inicial en el scratchpad** — nada se escribe en el repo todavía (regla
   "chat primero"). Sirve la carpeta con un servidor local (`.claude/launch.json` +
   `preview_start`) y verifica en el navegador.
2. **Verificar como si fueras el espectador.** Congela la línea de tiempo en los momentos
   clave con la Web Animations API y captura; pero recuerda que leer estilos con JS
   fuerza recálculos que enmascaran fallos de pintado — las comprobaciones de movimiento
   real se hacen con reproducción de verdad, y las de geometría (alineaciones) midiendo
   `getBoundingClientRect`, no a ojo.
3. **Iterar con el founder** hasta el visto bueno explícito. Entregas el HTML por el chat
   en cada versión relevante.
4. **Exportar solo tras aprobación** (ver abajo). Si el founder pide un cambio después,
   se edita la fuente, se reempaqueta y se regeneran únicamente las escenas afectadas —
   y se borran los MP4 viejos si lo pide.

## Exportación a video

Usa el pipeline del repo (`01-diseno/herramientas/`), nunca grabación en tiempo real:

1. Copia la pieza a `assets/<AAAA-MM>/<slug-del-reel>-escenas/` como `escenas.html` con
   su CSS extraído a `estilos.css` (el `@import` de Google Fonts al frente, que es lo que
   `empaquetar.py` sustituye por woff2 incrustados).
2. `python3 empaquetar.py <pieza>` → `escenas-completo.html` autocontenido.
3. Por cada escena: `python3 exportar-video.py escenas-completo.html --params "escena=N"
   --tamano 1080x1920 --fps 30 --salida video/formelia-<pieza>-escena-N-1080x1920.mp4`.
   La pieza debe cumplir el contrato de captura (`?limpio&zoom&escena`, `congelar()`,
   `DURACION_MS`, `dataset.listo`) — la plantilla ya lo trae.
4. **Verifica el resultado**: `ffprobe` (medidas, duración, fps) y extrae 1-2 fotogramas
   por escena con `ffmpeg -ss` para inspección visual real del MP4.
5. `assets/` está fuera de git: registra la pieza en el inventario de
   `assets/README.md` y recuerda que compartir es por Drive, no por el repo.

## Al terminar

Actualiza "Últimos movimientos" de `00-core/memoria.md` si la sesión fue significativa.
Si descubriste una trampa nueva del navegador o del pipeline, añádela a
`references/sistema.md` de este skill: la próxima sesión no debe redescubrirla.
