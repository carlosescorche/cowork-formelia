# Formelia HQ — Entorno de gestión de la empresa

Este repositorio es el **cuartel general de Formelia como empresa**. Aquí vive todo lo que no es
código: propósito, estrategia, marca, operaciones, diseño, marketing, growth, producto y
arquitectura. El producto y su documentación técnica viven en
[`formelia-app`](../formelia-app) — este repo gobierna *la empresa que opera ese producto*.

> **Qué es Formelia:** la plataforma AI-first de formularios y captura de datos para el mundo
> hispanohablante. "Describe tu formulario y la IA lo crea." Free $0 · Pro $10 · Team $25.
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
│                       métricas, memoria viva, log de decisiones — e incluye:
│   ├── marca/          Identidad de marca: estrategia, identidad visual, voz y tono
│   └── operaciones/    Legal y finanzas: bloqueantes de lanzamiento, economía de IA
├── 01-diseno/          Diseño: producción de piezas, plantillas y assets (ejecuta la marca)
├── 02-marketing/       Marketing: estrategia (en reinicio), calendario editorial, redes,
│                       campañas, blog/SEO
├── 03-growth/          Distribución y crecimiento: canales, experimentos, partners, comunidades
├── 04-producto/        Producto: PRDs, priorización, UX (el código vive en formelia-app)
├── 05-arquitectura/    Arquitectura: specs técnicos, ADRs, seguridad, costos de IA
└── .claude/skills/     Un skill (rol experto) por equipo
```

## Skills disponibles

| Skill | Rol | Trabaja sobre |
| --- | --- | --- |
| `/ceo` | CEO / estratega principal (incluye marca y operaciones) | `00-core/` |
| `/diseno` | Diseñador | `01-diseno/` |
| `/marketing` | Estratega de marketing y contenidos | `02-marketing/` |
| `/growth` | Growth lead | `03-growth/` |
| `/producto` | Product manager | `04-producto/` |
| `/arquitectura` | Arquitecto de software | `05-arquitectura/` |

## Relación con `formelia-app`

La estrategia fundacional está escrita e investigada en
[`formelia-app/docs/vision/`](../formelia-app/docs/vision/) (11 documentos, fechados
12-jul-2026): misión, mercado, 13+ competidores con pricing verificado, nicho y PMF,
diferenciación, plan 10x, roadmap 2026–2029. **Este repo la operacionaliza, no la reescribe.**
Los documentos de `00-core/` resumen lo decidido y enlazan a la fuente; cuando una decisión
nueva contradiga esos docs, se registra aquí y luego se sincroniza allá.
