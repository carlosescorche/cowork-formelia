# Assets de diseño

Assets producidos y reutilizables: exports de logo, plantillas por formato, iconografía,
OG images, recursos de landing.

## Convención

- Un subdirectorio por tipo: `logo/`, `plantillas/`, `og/`, `iconos/`.
- Nombrado: `slug-variante.ext` (p. ej. `logo-horizontal-teal.svg`).
- Toda plantilla lleva un `.md` hermano con su especificación (medidas, colores hex,
  tipografías, composición).

Las especificaciones de identidad que gobiernan estos assets están en
[`00-core/marca/`](../../00-core/marca/).

## Inventario

| Asset | Qué es | Estado |
| --- | --- | --- |
| [`plantillas/carrusel/`](plantillas/carrusel/carrusel.md) | Sistema de carruseles para Instagram y LinkedIn: tokens, composición, siete tipos de lámina y montaje de ejemplo. Se sincroniza con el proyecto de Claude Design. | En uso desde 2026-08-10 |
| [`plantillas/carrusel/` — línea editorial](plantillas/carrusel/carrusel-editorial.md) | Segundo repertorio alineado con el rediseño de la landing: arte pictórico, numerales contorneados, placas y banda de cierre con grano. Convive con la línea actual sin modificarla. | En uso desde 2026-08-11 |
| `plantillas/carrusel/arte/` | Espejo de los siete cuadros de `formelia-app/public/marketing/`. La fuente es el repo del producto. | Espejo, re-copiar si cambia |
| [`plantillas/motion-identidad/`](plantillas/motion-identidad/motion-identidad.md) | Motion de presentación de marca: el isotipo se construye, cuenta qué hace Formelia y se abre al logotipo. Crema y teal, en 3:4 y 9:16. CSS puro. | En uso desde 2026-08-12 |
| `logo/` | Exports del logo (SVG + PNG, claro/oscuro) | Pendiente |

Los archivos que producen estas plantillas (MP4, PNG) no se versionan: van a
[`assets/`](../../assets/README.md) en la raíz, que está en `.gitignore`. Las herramientas
que las empaquetan y las graban a vídeo están en
[`01-diseno/herramientas/`](../herramientas/README.md).
