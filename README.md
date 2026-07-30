# Formelia HQ — Entorno de gestión de la empresa

Este repositorio es el **cuartel general de Formelia como empresa**. Aquí vive todo lo que no es
código: propósito, estrategia, marca, marketing, comunicación, growth, research y operaciones.
El producto y su documentación técnica viven en [`formelia-app`](../formelia-app) — este repo
gobierna *la empresa que opera ese producto*.

> **Qué es Formelia:** la plataforma AI-first de formularios y captura de datos para el mundo
> hispanohablante. "Formularios que la gente sí termina." Free $0 · Pro $10 · Team $25.
> Lanzamiento público objetivo: **15-ago-2026**.

## Cómo funciona este repo

1. **`00-core/` es la fuente de verdad.** Propósito, visión, estrategia, posicionamiento y
   métricas. Todo lo que decide el CEO se registra en `00-core/decisiones/`. Ningún área puede
   contradecir lo que dice core; si hay conflicto, se resuelve con una decisión nueva.
2. **Cada carpeta numerada es un equipo.** Su `estrategia.md` es el documento vivo del área:
   define cómo trabaja ese equipo y a partir de él se ejecuta todo. Se actualiza con fecha cada
   vez que cambia algo.
3. **Las subcarpetas de cada área almacenan el trabajo producido** (piezas de contenido, briefs,
   entrevistas, experimentos, informes). Cada subcarpeta tiene un README con convenciones de
   nombrado.
4. **`.claude/skills/` contiene un skill por equipo.** Invocar un skill activa el rol experto de
   esa área: lee su estrategia, trabaja dentro de su carpeta y actualiza la memoria core.

## Estructura

```
cowork/
├── 00-core/            Dirección (CEO): propósito, visión, estrategia, posicionamiento,
│                       métricas, memoria viva y log de decisiones
├── 01-marca/           Marca y diseño: estrategia de marca, identidad visual, voz y tono, assets
├── 02-marketing/       Marketing: estrategia, calendario editorial, redes (una carpeta por red),
│                       campañas, blog/SEO
├── 03-comunicacion/    Comunicación: email, prensa, comunidad
├── 04-growth/          Distribución y crecimiento: canales, experimentos, partners
├── 05-research/        Investigación: competencia, entrevistas a usuarios, mercado
├── 06-operaciones/     Operaciones: legal, finanzas
└── .claude/skills/     Un skill (rol experto) por equipo
```

## Skills disponibles

| Skill | Rol | Trabaja sobre |
| --- | --- | --- |
| `/ceo` | CEO / estratega principal | `00-core/` |
| `/marca` | Director de marca y diseño | `01-marca/` |
| `/marketing` | Estratega de marketing y contenidos | `02-marketing/` |
| `/comunicacion` | Responsable de comunicación | `03-comunicacion/` |
| `/growth` | Growth lead | `04-growth/` |
| `/research` | Analista de investigación | `05-research/` |
| `/operaciones` | Operaciones, legal y finanzas | `06-operaciones/` |

## Relación con `formelia-app`

La estrategia fundacional está escrita e investigada en
[`formelia-app/docs/vision/`](../formelia-app/docs/vision/) (11 documentos, fechados
12-jul-2026): misión, mercado, 13+ competidores con pricing verificado, nicho y PMF,
diferenciación, plan 10x, roadmap 2026–2029. **Este repo la operacionaliza, no la reescribe.**
Los documentos de `00-core/` resumen lo decidido y enlazan a la fuente; cuando una decisión
nueva contradiga esos docs, se registra aquí y luego se sincroniza allá.
