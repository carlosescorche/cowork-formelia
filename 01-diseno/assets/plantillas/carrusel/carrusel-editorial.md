# Línea editorial de carruseles

> Documento vivo. Última actualización: 2026-08-11
> Variantes alineadas con el rediseño de la landing de agosto de 2026.
> **No sustituye a [`carrusel.md`](carrusel.md).** Convive con él: la línea actual sigue
> intacta y sigue siendo la de por defecto.

## Qué es

Un segundo repertorio de láminas que aplica el lenguaje visual del rediseño: arte pictórico de
fondo, placas de crema, numerales contorneados, el par de texto del mismo tamaño y la banda de
cierre con grano. Sirve para carruseles que tienen que sonar a la web nueva — presentación de
producto, recorridos, piezas de lanzamiento.

Todo cuelga de la clase `linea-editorial`, que se añade al mismo `.lienzo`. Sin esa clase, nada
cambia. El lienzo, la rejilla, las zonas seguras, el pie y las reglas de copy **se heredan sin
tocar** de `carrusel.md`: esto es dirección de arte nueva sobre la misma estructura.

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="carrusel.css">
<link rel="stylesheet" href="carrusel-editorial.css">
...
<div class="lienzo linea-editorial esquema-claro"> ... </div>
```

## De dónde sale cada patrón

Extraído del código del rediseño, no de capturas. Fuentes en `../formelia-app`:

| Patrón | Origen |
| --- | --- |
| Placa de crema con panel de arte y ventana encima | `sections/showcase/ShowcaseLayout.tsx` |
| Par título/cuerpo del mismo tamaño | `sections/showcase/ShowcaseLayout.tsx` |
| Numeral fantasma contorneado | `sections/HowItWorksSection.tsx` |
| Etiqueta de sección en píldora | `SectionHeading/SectionHeading.tsx` |
| Banda de cierre con grano y manchas | `sections/FinalCtaSection.tsx` |
| Receta del grano | `common/NoiseTexture/NoiseTexture.module.css` |
| Píldoras y gradiente diagonal de la llamada | `sections/HeroSection.tsx`, `marketing.css` |

## Los patrones, uno a uno

**1. El par editorial.** Título y cuerpo **del mismo tamaño** (44 px), los dos en Lexend. La
jerarquía la hace el color y el peso: título Medium en negro, cuerpo Regular en gris. Se leen
como un solo párrafo que se va apagando. Es el cambio de fondo respecto a la línea actual, donde
el título es casi el doble que el cuerpo.

**2. Numeral fantasma.** Lexend ExtraBold a 260 px, sin relleno, contorno de 4 px en teal-300
(teal-400 sobre oscuro). Es el ancla visual del paso; el título va debajo y en pequeño.

**3. Placa y panel de arte.** Caja de crema-100 al 60 % con 20 px de aire, y dentro un panel con
el arte a sangre y la ventana de producto flotando encima. El arte admite modo difuminado
(escala 1.25, desenfoque 40 px, saturación 1.15), que lo convierte en un lavado de color en vez
de un paisaje reconocible.

**4. Etiqueta de sección.** Píldora teal-50 con borde teal-100 y texto teal-700 en versalitas.
Sobre oscuro pasa a crema translúcido.

**5. Banda de cierre.** Teal-950 con radio de 64 px, grano al 5 % y dos manchas orgánicas
desenfocadas al 40 % (teal-700 arriba a la izquierda, teal-500 abajo a la derecha). Texto
centrado y píldoras completamente redondeadas.

**6. Título de sección.** Lexend **Regular** a 62 px con tracking cerrado. El rediseño baja el
peso de los títulos de sección; no van en Bold.

## Tipografía de la línea

| Rol | Fuente | Tamaño | Peso | Color |
| --- | --- | --- | --- | --- |
| Display (portada y cierre) | Lexend | 84 px | 700 | cream-50 |
| Título de sección | Lexend | 62 px | 400 | gray-950 |
| Par: título | Lexend | 44 px | 500 | gray-950 |
| Par: cuerpo | Lexend | 44 px | 400 | gray-600 |
| Numeral | Lexend | 260 px | 800 | contorno teal-300 |
| Subtítulo | Lexend | 34 px | 400 | crema al 78 % |
| Enlace de acento | Geist | 30 px | 500 | teal-700 |
| Etiqueta | Geist | 22 px | 600 | teal-700, versalitas |

## El arte

Siete piezas en [`arte/`](arte/), **espejo de `formelia-app/public/marketing/`**. La fuente es el
repo del producto: si la landing cambia sus cuadros, hay que volver a copiarlos aquí. No se
editan en este lado.

| Pieza | Medidas | Uso en 4:5 |
| --- | --- | --- |
| `art-basin` | 1200 x 1200 | A sangre, nítida |
| `art-mist` | 1200 x 1200 | A sangre, nítida |
| `art-deep` | 1376 x 768 | Solo difuminada o dentro de placa |
| `art-lake` | 1376 x 768 | Solo difuminada o dentro de placa |
| `art-meadow` | 1376 x 768 | Solo difuminada o dentro de placa |
| `art-sea` | 1376 x 768 | Solo difuminada o dentro de placa |
| `art-warm` | 1376 x 768 | Solo difuminada o dentro de placa |

**Regla:** cinco de las siete son apaisadas. Recortarlas a 4:5 nítidas se come el encuadre y
deja un fragmento sin composición. A sangre y nítidas solo van las dos cuadradas; las apaisadas
se usan difuminadas (donde el encuadre ya no importa) o dentro de una placa, que respeta su
proporción.

## Reglas propias de la línea

1. **El velo va donde va el texto.** Cualquier lámina con texto sobre arte lleva velo de
   legibilidad. Por defecto pesa abajo; con `velo-arriba` pesa arriba. Ponerlo al revés deja el
   texto claro sobre las zonas claras del cuadro y no se lee. Esto no es opcional.
2. **En 4:5 no hay zigzag.** La landing alterna texto e imagen de izquierda a derecha. En
   vertical, el panel va arriba y la copia debajo, siempre.
3. **Sin iconos, también aquí.** La landing usa iconografía funcional porque es interfaz de
   producto. Un carrusel es contenido, y ahí la regla de marca prohíbe pictogramas: la flecha se
   escribe (`→`), no se dibuja.
4. **Centrado solo en la banda de cierre.** Es la única lámina centrada del sistema entero, y es
   deliberado: cierra igual que cierra la web. Todo lo demás sigue alineado a la izquierda.
5. **Una sola llamada a la acción.** La segunda píldora del cierre es una salida discreta
   (preguntas frecuentes), no un segundo empujón.
6. **Capturas reales.** La ventana de la placa se rige por lo mismo que la línea actual: captura
   real o la lámina no está terminada.

## Qué no se hereda de la landing

- La marquesina de casos de uso: en un carrusel no hay movimiento.
- Las rejillas densas de capacidades (tres columnas de texto menudo): por debajo del mínimo de
  24 px del sistema.
- Los iconos de lucide.

## Variantes disponibles

| Archivo | Variantes |
| --- | --- |
| `10-editorial-portada.html` | Arte nítido, arte difuminado, promesa corta |
| `11-editorial-pasos.html` | Numeral sobre crema, numeral sobre arte, título de sección |
| `12-editorial-placa.html` | Arte nítido, arte difuminado, placa sobre oscuro |
| `13-editorial-cierre.html` | Banda con dos píldoras, banda con una, cierre claro con píldora sólida |

## Riesgos abiertos

- **El rediseño está sin publicar.** Al 2026-08-11, los cambios de la landing están sin commitear
  en `formelia-app`. Si el rediseño se mueve antes de cerrarse, esta línea se desalinea. Conviene
  revisarla cuando la landing entre a la rama principal.
- **El arte es un espejo.** Nadie avisa cuando la fuente cambia. Va en la revisión de campaña.
- **Convivencia sin regla de uso.** Falta decidir qué carruseles van en línea actual y cuáles en
  editorial. Hasta que se decida, la de por defecto sigue siendo la actual.

## Historial de cambios

- 2026-08-11 — Versión inicial: cuatro plantillas, doce variantes, hoja `carrusel-editorial.css`
  y espejo del arte de la landing.
