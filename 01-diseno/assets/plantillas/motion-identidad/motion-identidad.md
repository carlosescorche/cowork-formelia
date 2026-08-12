# Motion de identidad

> Última actualización: 2026-08-12 · Pieza en uso desde 2026-08-12
> Gobierna: [`00-core/marca/identidad-visual.md`](../../../../00-core/marca/identidad-visual.md)

Animación de presentación de marca: el isotipo se construye, cuenta qué hace Formelia y
se abre al logotipo completo. Es la pieza de apertura de las cuentas de redes.

## Qué entrega

| Archivo | Qué es |
| --- | --- |
| `motion-identidad.html` | La pieza. Las dos variantes van sincronizadas en la misma página. |
| `motion-identidad.css` | Tokens, composición y el reloj completo. |
| `formas.py` | Genera las formas de partida del isotipo. Solo si cambia la marca. |
| `exportar.sh` | Los cuatro comandos de exportación a MP4. |

Los MP4 no se versionan: van a [`assets/motion-identidad/`](../../../../assets/README.md),
que está en `.gitignore`.

## Lienzo y formatos

- Máster **1080 x 1440 px (3:4)**, para el feed de Instagram.
- **1080 x 1920 px (9:16)** para Reels y TikTok, con `?formato=9x16`: el lienzo crece y la
  escena de 1440 se centra dentro. No es el 3:4 con relleno — el fondo y el grano cubren
  todo el alto, así que no hay banda negra ni costura.
- Ciclo de **16 500 ms**, en bucle. 495 fotogramas a 30 fps.
- Dos variantes: **crema** (`--cream-50`) y **teal** (`--teal-950`).
- **Fondo transparente** con `?fondo=transparente`, para montar la pieza sobre otro
  material. Se cae el fondo y el grano; la tinta la sigue fijando la variante, así que
  `solo=crema` da tinta oscura (para claro) y `solo=teal` tinta clara (para oscuro).
  Ver [Transparencia](#transparencia) antes de usarlo.

## Línea de tiempo

| Tramo | Qué pasa |
| --- | --- |
| 0,15 – 1,11 s | Aparece un solo rombo curvo, traslúcido |
| 1,11 – 2,00 s | Se divide en dos y las curvas se tensan a rombos rectos |
| 2,25 – 2,71 s | La mordida: los rombos pierden esquinas y sale el isotipo |
| 2,85 – 3,55 s | La caja de selección encaja sobre él y lo rotula `01_isotipo` |
| 3,95 – 6,20 s | Entra el prompt y se teclea · `02_describe` |
| 7,05 – 8,11 s | La IA levanta el formulario, campo a campo · `03_generando` |
| 8,95 – 10,56 s | La gente lo responde y lo envía · `04_completado` |
| 11,45 – 12,11 s | Vuelve el isotipo, a escala media · `05_logotipo` |
| 12,75 – 14,15 s | Se abre paso al logotipo y se revela el wordmark |
| 14,41 – 16,50 s | Entra el dominio y cierra en firme |

El último fotograma queda limpio —logotipo y `formelia.io`, sin caja ni rótulo— porque es
el que se ve como portada en el feed.

## Decisiones de construcción

**Un solo reloj.** Cada animación dura 16 500 ms, es `infinite` y coloca su tramo con
porcentajes. Ninguna usa `animation-delay` para secuenciar. De ahí salen tres propiedades:
la pieza se reproduce y se repite **sin una línea de JavaScript**, todo queda en fase entre
ciclos, y cualquier instante se puede congelar con `currentTime` para capturar vídeo.

**El JavaScript es opcional.** Solo añade los controles, el ajuste fino de medidas y el
congelado por `?t=`. Si el visor no ejecuta scripts, la animación funciona igual. El
marcado de las dos escenas está escrito en el HTML, no generado.

**El wordmark va trazado**, nunca como texto vivo: la pieza se renderiza idéntica aunque no
cargue ninguna tipografía. Lexend y Geist solo hacen falta para el prompt, el formulario y
los rótulos.

**El isotipo son dos capas.** No es una forma con partes: es la misma pieza repetida con un
desplazamiento diagonal de (+24,66, +42,95) que se tocan en una sola esquina, (82,7 · 102,1).
Partir el path maestro por esa esquina las separa sin alterar un solo punto de la marca —
verificado superponiendo el original debajo de las dos capas.

**La apertura sale de esa geometría.** Un rombo curvo único se divide en dos, cada mitad
viaja a su sitio, se tensa a rombo recto y pierde las esquinas hasta ser su capa. El rombo
curvo es el gesto con el que el mundo dibuja la IA; que se divida en dos y aterrice en la
marca dice lo mismo que el producto: describes una vez y sale la pieza.

## Formas de partida

Las genera `formas.py` y están escritas en los `@keyframes capa-abajo` y `capa-arriba`.
Solo hace falta volver a correrlo si cambia la marca o si se quiere otra forma de partida.

Parámetros con los que se generaron las de hoy: rombo `r 39.6` · rombo curvo `r 46`,
concavidad `0.38`.

CSS interpola la propiedad `d` solo si los dos paths comparten estructura de comandos
(mismos M/L/C/Z en el mismo orden), así que el script no dibuja un rombo cualquiera:
reparte las anclas del path real sobre el perímetro de la forma destino respetando la
fracción de recorrido y el sentido de giro, clava cuatro de ellas en las esquinas y saca
los puntos de control subdividiendo la curva de cada lado.

## Ajustes disponibles

| Qué | Dónde |
| --- | --- |
| Opacidad del estado traslúcido | `--capa-tenue`: 0,42 en crema, 0,34 en teal |
| Concavidad y radio del rombo curvo | `formas.py`, arriba del todo |
| Texto del prompt y del formulario | En el HTML, en las dos escenas |
| Ritmo de cualquier tramo | Porcentajes de los `@keyframes`, sobre 16 500 ms |

Los rótulos usan minúscula con guion bajo, a la manera de un archivo de diseño:
`01_isotipo`, `02_describe`, `03_generando`, `04_completado`, `05_logotipo`.

## Transparencia

**No sirve para publicar.** Instagram y TikTok aplanan el alfa, y MP4/H.264 ni siquiera
tiene canal para guardarlo. La transparencia es para **componer**: superponer la marca
sobre vídeo propio, meterla en una presentación o en la web.

Dos entregables, según destino:

| Formato | Códec | Para qué | Peso |
| --- | --- | --- | --- |
| `.mov` | ProRes 4444 | Editar (Premiere, Final Cut, After Effects, DaVinci) | ~55 MB |
| `.webp` | WebP animado | Web y navegador | ~1,7 MB |

No hay versión `.webm`: ffmpeg 7.1 pierde el alfa en VP9 sin avisar (detalle en el
[README de herramientas](../../../herramientas/README.md#transparencia)).

```bash
python3 ../../../herramientas/exportar-video.py motion-identidad-completo.html \
  --alfa --tamano 1080x1440 --params "solo=crema&fondo=transparente" \
  --salida ../../../../assets/motion-identidad/formelia-motion-tinta-oscura-1080x1440.mov
```

**Qué aguanta bien y qué no.** Los momentos de marca —la construcción del isotipo, el
logotipo, el dominio— son formas sólidas y se montan sobre cualquier cosa. El tramo
central no: el prompt y el formulario se diseñaron para descansar sobre un fondo sólido,
así que sus superficies (`--superficie`, blanco al 55 %) se tiñen de lo que haya detrás y
los rótulos en gris pierden legibilidad sobre material con textura o color fuerte.

Sobre metraje oscuro y quieto funciona; sobre metraje claro o movido, el tramo central se
lava. Si hace falta un recurso de superposición de verdad, lo suyo es una versión corta
con solo los tramos de marca, no esta pieza entera con el fondo quitado.

## Cómo se produce

```bash
# 1. Empaquetar en un HTML autocontenido (incrusta CSS y tipografías)
python3 ../../../herramientas/empaquetar.py motion-identidad.html

# 2. Sacar los cuatro MP4
./exportar.sh
```

Para revisarla sin exportar, abrir `motion-identidad.html` en el navegador. Controles y
parámetros de URL:

| Parámetro | Para qué |
| --- | --- |
| `?solo=crema` / `?solo=teal` | Aislar una variante |
| `?formato=9x16` | Lienzo de 1080 x 1920 |
| `?zoom=1` | Tamaño real |
| `?limpio=1` | Sin cabecera ni controles |
| `?t=8300` | Congelar en ese milisegundo |

## Límites conocidos

- **El morfado de la apertura solo lo interpolan Chrome y Edge.** Es donde capturamos el
  vídeo, así que no afecta al entregable; en otros navegadores la apertura salta entre los
  tres estados en vez de fluir. El resto de la pieza va bien en todos.
- **Los MP4 salen sin pista de audio.** La música se pone en la app al publicar.
- **Si Instagram recorta el 3:4 en el feed**, el formato seguro es 4:5 (1080 x 1350). Se
  saca añadiendo un modo equivalente al de 9:16.

## Historial de cambios

- 2026-08-12 — Versión inicial. Apertura por división del rombo curvo, elegida entre once
  alternativas exploradas.
