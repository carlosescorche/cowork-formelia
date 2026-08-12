# Sistema de carruseles

> Documento vivo. Última actualización: 2026-08-10
> Especificación hermana de los archivos de esta carpeta. Gobierna todos los carruseles de
> Formelia: Instagram (@joinformelia) y LinkedIn de marca.
>
> Manda por encima de este documento: [`00-core/marca/identidad-visual.md`](../../../../00-core/marca/identidad-visual.md)
> y [`00-core/marca/voz-y-tono.md`](../../../../00-core/marca/voz-y-tono.md). La fuente canónica
> de color y tipografía es `../formelia-app/docs/design/`.

## Qué hay en esta carpeta

| Archivo | Qué es |
| --- | --- |
| `carrusel.md` | Esta especificación. Lo que no esté aquí, no está decidido. |
| `tokens.css` | Variables: paleta, escala tipográfica, rejilla, radios, sombras, esquemas. |
| `carrusel.css` | Clases de composición de lámina. |
| `00-fundamentos.html` | Lienzo con guías, paleta y muestrario tipográfico. |
| `01-portada.html` | Portada: oscura, clara y de promesa corta. |
| `02-contenido.html` | Lámina intermedia: título y cuerpo, lista, frase de ejemplo. |
| `03-dato.html` | Lámina de cifra y lámina de cita. |
| `04-captura.html` | Marcos de teléfono y de navegador para capturas reales. |
| `05-cierre.html` | Última lámina, con y sin llamada a la acción de marca. |
| `ejemplo-4c.html` | Las siete láminas de la Pieza 4C montadas de principio a fin. |

Desde el 2026-08-11 existe además una **[línea editorial](carrusel-editorial.md)**: un segundo
repertorio de láminas alineado con el rediseño de la landing (arte de fondo, numerales
contorneados, banda de cierre con grano). Convive con este sistema y no lo modifica; se activa
añadiendo la clase `linea-editorial` al lienzo. Lo de aquí sigue siendo lo de por defecto.

Todo se dibuja a tamaño real (1080 x 1350 px) y se previsualiza con `--zoom`. Para exportar,
`--zoom: 1`.

## Formatos y export

| Destino | Medida | Formato | Notas |
| --- | --- | --- | --- |
| Instagram carrusel | 1080 x 1350 px (4:5) | PNG, sRGB | Medida de diseño nativa. |
| LinkedIn documento | 1200 x 1500 px (4:5) | PDF | Mismo arte escalado x1.111. |
| LinkedIn imagen | 1080 x 1350 px (4:5) | PNG, sRGB | Sin cambios. |

Un solo arte para las dos redes: la proporción es la misma. Nombrado de export:
`AAAA-MM-DD-campana-slug-NN.png` (`NN` = número de lámina con cero delante).

## Lienzo, rejilla y zonas seguras

- **Lienzo:** 1080 x 1350 px.
- **Margen exterior:** 90 px por los cuatro lados. Área viva: 900 x 1170 px.
- **Rejilla horizontal:** 6 columnas de 125 px con medianiles de 30 px.
- **Ritmo vertical:** todo espaciado es múltiplo de 30 px.
- **Medida de línea del cuerpo:** máximo 840 px (deja aire a la derecha; el texto a sangre
  completa se lee peor en móvil).

Zonas seguras:

1. **Banda superior, 120 px:** nada esencial. Es donde recorta el visor de LinkedIn.
2. **Banda inferior, 180 px:** nada esencial salvo el pie, que está diseñado para vivir ahí.
   El visor de documentos de LinkedIn superpone su contador de páginas en esa franja.
3. **Recorte cuadrado de la portada:** el display y el antetítulo de la lámina 1 tienen que
   caber en los 1080 x 1080 px centrales (de y=135 a y=1215) para aguantar cualquier superficie
   que muestre la pieza en 1:1.

Las guías se ven añadiendo la clase `guias` al contenedor. **Nunca se exportan.**

## Color

Dos esquemas y ninguno más. Un carrusel usa oscuro en portada y cierre, y claro en todo el
contenido intermedio. Alternar esquema entre láminas de contenido está prohibido: el ojo lee el
cambio de fondo como cambio de tema.

| Rol | Claro (contenido) | Oscuro (portada y cierre) |
| --- | --- | --- |
| Fondo | cream-50 `#f8f5f0` | teal-950 `#022f2e` |
| Título | teal-900 `#0a4d4d` | cream-50 `#f8f5f0` |
| Cuerpo | gray-800 `#383838` | teal-100 `#d1eeee` |
| Acento | teal-700 `#00786f` | teal-400 `#00d5be` |
| Pie y textos tenues | gray-600 `#6b6b6b` | cream-50 al 62% |
| Líneas y pistas | cream-200 `#e5ded0` | cream-50 al 16% |

Reglas heredadas de marca, sin excepción:

1. El acento de acción es siempre teal, y hay **uno solo por lámina**.
2. Éxito es teal, nunca verde.
3. La IA no se pinta de violeta ni se marca con destellos. Grises neutros.
4. Sin azul corporativo. Si la lámina podría ser de cualquier SaaS, se rehace.
5. Blanco puro solo dentro de las capturas y de sus marcos. El fondo de lámina nunca es blanco.

## Tipografía

Lexend para títulos, Geist para cuerpo. Valores a escala de lienzo (1080 px):

| Rol | Fuente | Tamaño | Peso | Interlineado | Tracking | Tope |
| --- | --- | --- | --- | --- | --- | --- |
| Display (portada) | Lexend | 92 px | 700 | 1.06 | -0.02em | 8 palabras |
| Display corto | Lexend | 118 px | 700 | 1.06 | -0.02em | 5 palabras |
| Título de lámina | Lexend | 68 px | 600 | 1.12 | -0.015em | 8 palabras |
| Título largo | Lexend | 56 px | 600 | 1.12 | -0.015em | 12 palabras |
| Cifra | Lexend | 150 px | 700 | 1.0 | -0.03em | — |
| Cita | Lexend | 54 px | 500 | 1.25 | -0.01em | 16 palabras |
| Cuerpo | Geist | 38 px | 400 | 1.42 | 0 | 28 palabras |
| Cuerpo secundario | Geist | 30 px | 400 | 1.45 | 0 | — |
| Antetítulo | Geist | 24 px | 600 | 1.0 | 0.12em, versalitas | 4 palabras |
| Pie y paginación | Geist | 24 px | 500 | 1.0 | 0.02em | — |

- Un solo tamaño de título por carrusel: o todas las láminas usan 68 o todas usan 56.
- Nada por debajo de 24 px. A esa escala, 24 px equivale a 12 px en pantalla de móvil.
- Las fuentes se cargan desde Google Fonts en `tokens.css`. Si el entorno bloquea recursos
  externos, la pieza cae a la pila del sistema y **no sirve para exportar**: hay que instalar
  Lexend y Geist en local antes de sacar el PNG.

## Tipos de lámina

| Tipo | Cuándo | Archivo |
| --- | --- | --- |
| Portada | Lámina 1, siempre | `01-portada.html` |
| Título y cuerpo | El caballo de batalla del contenido | `02-contenido.html` |
| Lista | Pasos o enumeraciones, máximo 4 ítems | `02-contenido.html` |
| Frase de ejemplo (chip) | Cuando enseñas literalmente qué escribir | `02-contenido.html` |
| Cifra | Un dato propio y citable | `03-dato.html` |
| Cita | Voz de un usuario real | `03-dato.html` |
| Captura | Cuando hay que enseñar el producto | `04-captura.html` |
| Cierre | Última lámina, siempre | `05-cierre.html` |
| Cierre con captura | Cuando la última pantalla del recorrido **es** el remate y no cabe en una lámina aparte. Ancla arriba, marco de navegador compacto (780 px, recorte 16:9) y una sola llamada a la acción debajo. | `05-cierre.html` |

## Anclaje vertical

El bloque de contenido no se centra por defecto, y esto es deliberado: al deslizar, un bloque
centrado hace que el título suba y baje según lo largo que sea el cuerpo, y los títulos bailan.

| Tipo de lámina | Anclaje | Clase |
| --- | --- | --- |
| Contenido, lista, chip, captura | Arriba — el antetítulo arranca siempre en y=90 | (por defecto) |
| Portada y cierre | Abajo — el texto se apoya sobre el pie | `al-final` |
| Cierre con captura | Arriba — la captura necesita el alto | (por defecto) |
| Cifra y cita | Centrado — son láminas de respiro y el salto es intencional | `centrada` |

## Ritmo del carrusel

- **6 a 8 láminas. El óptimo es 7.** Menos de 6 no justifica el formato; más de 8 pierde a la
  gente antes del cierre.
- Lámina 1 portada, última cierre. En medio, **una idea por lámina**.
- **Regla de la lámina 2:** es donde se cae la gente. La 2 tiene que pagar lo que prometió la 1,
  no ser una introducción ni un "antes de empezar".
- Después de tres láminas seguidas de texto, entra una de respiro: cifra, cita o captura.
- La última lámina lleva **una sola llamada a la acción**. Nunca dos.

## Pie de lámina

- **Barra de progreso** de 6 px de alto, ancho del área viva, pista en cream-200 y relleno en
  teal-700. El porcentaje es `(n-1) / (total-1)`.
- **Firma** abajo a la izquierda: `formelia.io` en el contenido; `@joinformelia` en el cierre.
- **Paginación** abajo a la derecha: `3 / 7`. Números, nunca puntos.
- La portada no lleva progreso ni paginación: lleva `Desliza →` en el sitio de la paginación.
- El hueco del icono de marca está pendiente del export del SVG del logo (ver
  [`00-core/marca/identidad-visual.md`](../../../../00-core/marca/identidad-visual.md)). Hasta
  entonces la firma es solo wordmark en Lexend Medium.

## Capturas de producto

- **Siempre reales.** Nunca una interfaz dibujada ni una pantalla que el producto no tenga hoy.
- Teléfono: 560 px de ancho, radio 56 px, marco gray-950 de 14 px. Captura a 1170 x 2080.
- Navegador: 900 px de ancho, radio 28 px, borde gray-200. Captura a 1800 x 1350.
- El texto va arriba y la captura debajo. Nunca al revés: en móvil se lee de arriba abajo.
- El rayado diagonal (`hueco-captura`) es maqueta. Si una lámina llega a revisión con el rayado
  puesto, no está terminada.

## Copy

Manda [`voz-y-tono.md`](../../../../00-core/marca/voz-y-tono.md). Aplicado al carrusel:

1. Tuteo, imperativo, frases cortas. Nunca voseo.
2. El dolor primero, la solución después.
3. **Sin iconos ni emoji.** Los estados van con palabras. Las flechas (`→`) no son iconos.
4. **Informar, no vender.** "Gratis" solo puede aparecer dentro del botón de la lámina de
   cierre — es la llamada a la acción sancionada para las cuentas de marca. En títulos, cuerpos
   y en el texto del post está prohibida.
5. Nunca "en español" en una pieza escrita en español.
6. Nunca "Typeform con IA", "magia", "revolucionario" ni promesas de roadmap como si ya
   existieran.
7. La marca no habla en primera persona del founder. Si la pieza necesita "yo", va en las
   cuentas personales, no en @joinformelia.

## Checklist antes de publicar

1. Entre 6 y 8 láminas, portada y cierre en su sitio.
2. Un solo acento teal por lámina. Ningún verde, ningún violeta, ningún azul.
3. Todos los textos dentro del área viva; nada esencial en las bandas de 120 y 180 px.
4. La portada se sostiene recortada a 1:1.
5. Un solo tamaño de título en todo el carrusel.
6. Cero iconos y cero emoji.
7. Ninguna captura inventada; ningún rayado de maqueta.
8. Una sola llamada a la acción, en la última lámina.
9. "Gratis" solo dentro del botón de cierre, si es que aparece.
10. Fuentes Lexend y Geist realmente cargadas en el export.
11. Nombres de archivo `AAAA-MM-DD-campana-slug-NN.png`.

## Cómo se usa esto en Claude Design

El repo es la fuente de verdad; Claude Design es la superficie de trabajo. El ciclo:

1. Se edita aquí (`tokens.css`, `carrusel.css`, las láminas y este documento).
2. Se sube al proyecto de sistema de diseño con la herramienta `DesignSync`: primero
   `finalize_plan` con las rutas, después `write_files`. Cada HTML se anuncia en el panel con su
   marcador `@dsCard` de la primera línea, agrupado en "Carruseles".
3. En Claude Design se pide la pieza nueva apoyada en ese sistema: las láminas nuevas heredan
   tokens, composición y reglas sin volver a describirlas.
4. Lo que se aprenda montando piezas reales vuelve aquí. Un cambio que solo viva en Claude
   Design se pierde en la siguiente pieza.

Regla de frontera: **la identidad no se decide en Claude Design.** Si montando un carrusel
aparece la necesidad de un color, un peso o una medida que no existen en este documento, se
propone como cambio en `00-core/marca/` con fecha e historial, no se inventa en la pieza.

## Pendientes

- **Discrepancia detectada (2026-08-10):** `00-core/marca/identidad-visual.md` da teal-500 como
  `#159999`; la fuente canónica `formelia-app/docs/design/color-system.md` lo da como `#129f9f`.
  Este sistema usa el canónico. Queda pendiente unificar en marca.
- Icono del logo sin exportar a SVG estático: la firma y el cierre usan wordmark solo.
- Falta la variante de portada con captura, para carruseles que abren enseñando producto.

## Historial de cambios

- 2026-08-10 — Añadida la variante **cierre con captura**, con el marco de navegador compacto
  (780 px, recorte 16:9). Hueco descubierto al montar la Pieza 4A, que necesita rematar el
  recorrido y cerrar en la misma lámina.
- 2026-08-10 — Versión inicial del sistema de carruseles (tokens, composición, seis plantillas
  de lámina, montaje de ejemplo y especificación).
