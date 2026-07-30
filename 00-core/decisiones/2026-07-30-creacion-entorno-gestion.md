# Creación del entorno de gestión de la empresa (Formelia HQ)

- **Fecha:** 2026-07-30
- **Estado:** Vigente
- **Área(s) afectada(s):** todas

## Contexto

El producto está sustancialmente terminado y el lanzamiento es el 15-ago-2026. El diagnóstico
del plan 10x es explícito: el riesgo #1 es distribución y "lo que falta no es producto, es
empresa". La estrategia fundacional existe (`formelia-app/docs/vision/`, 11 docs) pero no había
un lugar donde operarla: ni estrategias por área, ni memoria de decisiones, ni almacenamiento
del trabajo de marketing/marca/comunicación.

## Decisión

Crear el repositorio `cowork/` como cuartel general de Formelia con: (1) `00-core/` como fuente
de verdad de dirección con log de decisiones y memoria viva; (2) un equipo por carpeta (marca,
marketing, comunicación, growth, research, operaciones), cada uno con su `estrategia.md` como
documento vivo y subcarpetas de almacenamiento; (3) un skill por equipo en `.claude/skills/` que
actúa como el rol experto de esa área.

## Alternativas consideradas

1. **Seguir usando `formelia-app/docs/`** — mezcla empresa con producto; el repo de código no es
   lugar para calendarios editoriales ni piezas de contenido.
2. **Herramienta externa (Notion, etc.)** — pierde versionado git, no es operable por agentes con
   skills, y fragmenta la memoria.

## Consecuencias

- Toda decisión de CEO se registra aquí a partir de hoy.
- Las áreas ejecutan desde su `estrategia.md`; los docs de visión de `formelia-app` quedan como
  investigación de respaldo y se sincronizan cuando una decisión los contradiga.
- Riesgo aceptado: duplicación parcial de contenido con `docs/vision/` — mitigado con enlaces a
  la fuente y la regla de "resumir, no reescribir".

## Criterio de revisión

Si al llegar la primera contratación (gate: ≥500 signups/mes orgánicos) el equipo necesita otra
herramienta de colaboración, revisar si este repo sigue siendo el HQ o pasa a ser el archivo.
