# Sistema de escenas animadas — referencia técnica

Cómo funciona el visor, el contrato de captura y las trampas de Chrome que ya nos
costaron una depuración. Empieza siempre desde `assets/plantilla.html`, que implementa
todo esto; esta referencia explica el porqué de cada pieza para que puedas modificarla
sin romperla.

## Índice

1. Arquitectura del visor
2. El mecanismo de pausa (`--ps`) y su recálculo forzado
3. Tipeo por caracteres
4. Secuencias con estados que van y vuelven (un solo reloj)
5. Contrato de captura para `exportar-video.py`
6. Trampas conocidas de Chrome
7. Cómo verificar sin engañarte

## 1. Arquitectura del visor

- Página oscura con una `.card` por escena: título, descripción corta, `stage-wrap` con
  el lienzo, barra de progreso y botones Reproducir / Pausar / Reiniciar.
- El lienzo (`.stage`) es SIEMPRE 1080×1920 reales, escalado con
  `transform: scale()` para caber en la tarjeta (la función `fit()` recalcula al
  redimensionar). Así el diseño se hace en píxeles finales y el export no re-escala nada.
- Cada escena declara su duración en segundos en `data-dur` de la tarjeta; la barra de
  progreso usa esa misma duración en su `animation-duration` inline.
- Contenido repetido se monta por JS al cargar (clonar un formulario entre escenas,
  generar filas vacías, construir el tipeo). Todo el montaje ocurre antes de que el
  usuario pueda dar a Reproducir, así que las animaciones CSS lo cubren igual.

## 2. El mecanismo de pausa y su recálculo forzado

Todas las animaciones nacen pausadas y se controlan con una variable heredada:

```css
.stage, .stage *, .progress > i {
  animation-play-state: var(--ps, paused) !important;
  animation-fill-mode: both !important;
}
.noanim * { animation: none !important; }
```

- Van con `!important` porque cualquier shorthand `animation:` de una escena
  **resetea** las longhands `play-state` y `fill-mode`; sin el important, cada
  escena se reproduciría sola al cargar.
- `fill-mode: both` hace que el fotograma 0% se vea antes del delay (estado inicial
  correcto de cada escena en reposo).
- El controlador escribe `--ps` en la **tarjeta** y fuerza un recálculo síncrono:

```js
card.style.setProperty("--ps", state);
void card.offsetWidth;                    // aplica el cambio YA y para todos
card.getAnimations({ subtree: true });    // materializa las animaciones
```

  Sin el recálculo, Chrome aplica el cambio de la variable tarde y **elemento a
  elemento**: los delays largos (el tipeo) quedan desincronizados o directamente no
  arrancan. Este fue un bug real; no quites esas dos líneas.
- Reiniciar = poner clase `noanim`, forzar reflow (`void stage.offsetWidth`), quitarla y
  volver a `running`. Eso destruye y recrea las animaciones CSS desde cero.

## 3. Tipeo por caracteres

El texto que "se escribe" se monta en JS: un `<span class="tchar">` por carácter con
`animation-delay` inline (`inicio + i * cadencia`). El span es `inline-block` con
`max-width: 0 → 1.2em` y `opacity: 0 → 1`, de modo que cada letra ocupa su ancho al
aparecer y un caret colocado al final del texto avanza solo.

- El elemento con el texto lleva `data-text`, `data-start` (ms) y `data-speed`
  (ms/carácter); el montador los recorre (`.typed` en la plantilla).
- La animación del carácter dura **90 ms con curva lineal e interpolación real**. No
  uses 1 ms + `steps()`: ver trampa 6.2.
- **Sin `overflow: hidden`** en el span: cambiaría su línea de base y desalinearía el
  texto respecto al caret y a los textos vecinos (trampa 6.3). La opacidad ya oculta el
  glifo mientras el ancho colapsa.
- El caret parpadea con una animación infinita; para que no se vea antes de tiempo va
  envuelto: el padre controla el "cuándo aparece" (delay + fill) y el hijo parpadea
  libre. Dos animaciones sobre el mismo elemento con fills que se pisan no funcionan
  (trampa 6.4).

## 4. Secuencias con estados que van y vuelven

Un elemento que pasa por varios estados (gris → activo → cargando, o entrar → salir)
no puede llevar una animación por estado: el `fill: both` global hace que el fill
"backwards" de la animación tardía pise a la temprana antes de su delay. Dos remedios:

- **Un solo reloj**: una única animación con la duración total de la escena y los
  estados colocados por porcentajes. Es lo que usa el botón de enviar de la demo
  (gris/teal/gris en un keyframes de 14 s).
- **Anidar**: entrada en el wrapper exterior, salida en el interior (patrón de los
  slides del respondent). Cada capa tiene un solo fill y no hay conflicto.

Las transiciones entre pantallas de la app se copian del código real. La del respondent
de Formelia (`QuestionSlideTransition.tsx`): salida `translateX(0→-40px)` + fade en
0.3 s, entrada `translateX(40px→0)` + fade en 0.35 s, ambas `cubic-bezier(.4,0,.2,1)`,
simultáneas.

## 5. Contrato de captura para exportar-video.py

La pieza debe aceptar `?limpio=1&zoom=1&escena=N&t=0` y exponer:

- `window.congelar(ms)` — pausa todas las animaciones de la escena activa vía WAAPI y
  las coloca en ese milisegundo (cachea la lista de `getAnimations({subtree:true})`).
- `window.DURACION_MS` — duración de la escena activa (de `data-dur` × 1000).
- `document.body.dataset.listo = "1"` — tras `document.fonts.ready` + un
  `requestAnimationFrame` (y tras remedir lo que dependa de fuentes), congelado en `t`.

En modo `limpio`: se elimina toda tarjeta que no sea la pedida, se quita la interfaz
del visor y el stage va a escala 1 en 1080×1920 (el exportador fija el viewport a ese
tamaño). La plantilla implementa todo esto.

El pipeline completo: `empaquetar.py` (fuentes de Google → woff2 base64; requiere que la
pieza enlace un CSS local cuyo primer statement sea el `@import` de Google Fonts) y
`exportar-video.py` (Chrome por CDP, un fotograma por `congelar()`, ffmpeg H.264 CRF 18
`+faststart`). Ambos documentados en `01-diseno/herramientas/README.md`.

## 6. Trampas conocidas de Chrome

1. **`--ps` sin recálculo forzado**: cambiar una custom property usada en
   `animation-play-state` no invalida estilos de los descendientes de forma fiable; sin
   `void offsetWidth` las animaciones arrancan tarde y desincronizadas (y las lecturas
   de estilos de tu propia verificación "lo arreglan" — efecto observador).
2. **Animaciones de ~1 ms con `steps()`**: si la fase activa cabe entera entre dos
   frames, Chrome puede darlas por terminadas sin pintarlas nunca, y no vuelve a
   recalcular ese elemento: el estado final no se ve hasta el siguiente recálculo
   (pausar, por ejemplo). Usa siempre duraciones reales interpoladas (60-120 ms lineal).
3. **`inline-block` + `overflow: hidden`**: mueve la línea de base del elemento a su
   arista inferior; el texto queda ~4 px desalineado respecto a sus vecinos inline.
4. **Dos animaciones con fill en el mismo elemento**: el fill backwards de la posterior
   gana antes de su delay. Ver sección 4.
5. **bfcache**: al re-navegar a la pieza, Chrome puede restaurar la página con las
   animaciones WAAPI-pausadas de una sesión de verificación anterior. Recarga con un
   query distinto (`?v=n`) antes de sacar conclusiones de un estado raro.
6. **Panel oculto**: con el visor no visible (`document.hidden`), Chrome no pinta; las
   capturas salen congeladas y los scrolls expiran. Verifica geometría por JS
   (`getBoundingClientRect`) cuando no puedas confiar en la captura.

## 7. Cómo verificar sin engañarte

- **Estados**: congela con WAAPI (`a.pause(); a.currentTime = t`) en los momentos clave
  y captura. Bueno para composición, no prueba el movimiento real.
- **Movimiento real**: click de verdad en Reproducir y capturas durante la reproducción,
  sin ejecutar JS entre medias (leer estilos fuerza recálculos que enmascaran fallos de
  pintado como la trampa 6.2).
- **Geometría** (alineaciones, cajas): mide con `getBoundingClientRect` y compara
  números; funciona incluso con el panel oculto.
- **El MP4 final**: `ffprobe` para medidas/duración/fps y `ffmpeg -ss T -frames:v 1`
  para extraer fotogramas del archivo real — lo que se verifica es el video, no la
  pieza.
