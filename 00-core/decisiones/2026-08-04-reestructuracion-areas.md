# Reestructuración de áreas y reinicio de la estrategia de marketing

- **Fecha:** 2026-08-04
- **Estado:** Vigente
- **Área(s) afectada(s):** todas

## Contexto

A cinco días de crear Formelia HQ, la estructura de siete áreas (marca, marketing,
comunicación, growth, research, operaciones) resultó más pesada que el equipo real que la
opera. Marca y operaciones no son equipos de ejecución sino reglas y compliance transversales;
comunicación y research duplicaban trabajo que pueden absorber growth y core. Además faltaban
las dos áreas que conectan HQ con el producto: producto y arquitectura. La estrategia de
marketing v1 y su primera pieza no convencieron y se prefiere reformular desde cero antes del
lanzamiento del 15-ago-2026.

## Decisión

Las áreas de ejecución quedan en cinco: **diseño, marketing, growth, producto y arquitectura**.
**Marca y operaciones pasan a `00-core/`** (custodiadas por el CEO). **Comunicación y research
se disuelven** (comunidades pasa a growth; entrevistas y vigilancia de competencia las coordina
core). **La estrategia de marketing se reinicia desde cero**: se descartan la v1, el calendario
editorial y las piezas producidas.

## Alternativas consideradas

1. **Mantener las 7 áreas** — estructura sobredimensionada para un founder solo; cada sesión
   pagaba el costo de navegar áreas sin actividad real.
2. **Ajustar la estrategia de marketing v1 en lugar de reiniciarla** — se prefiere partir de
   cero para no heredar decisiones (pilares, cadencias por red) tomadas sin datos.

## Consecuencias

- Estructura nueva: `00-core/` (con `marca/` y `operaciones/`), `01-diseno/`, `02-marketing/`,
  `03-growth/`, `04-producto/`, `05-arquitectura/`. Skills: `/ceo`, `/diseno`, `/marketing`,
  `/growth`, `/producto`, `/arquitectura`.
- `02-marketing/estrategia.md` queda en estado "por definir"; el calendario editorial vacío.
  **Riesgo aceptado conscientemente:** la semana teaser (4–14 ago) queda sin piezas hasta que
  la nueva estrategia esté escrita — redefinirla es el pendiente inmediato.
- Documentos actualizados: `README.md`, `CLAUDE.md`, `00-core/README.md`, `estrategia.md`,
  `metricas.md`, `memoria.md`, estrategias de las áreas nuevas.

## Criterio de revisión

Si al crecer el equipo (primeras contrataciones, ver gates en `00-core/estrategia.md`) alguna
función de core (marca, operaciones) o de growth (comunidades) necesita dueño dedicado, se
vuelve a separar como área con una decisión nueva.
