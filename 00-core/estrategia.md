# Estrategia — corto, mediano y largo plazo

> Última actualización: 2026-07-30 · Fuentes:
> [`docs/vision/07-plan-transformacion-10x.md`](../../formelia-app/docs/vision/07-plan-transformacion-10x.md),
> [`docs/vision/08-roadmap.md`](../../formelia-app/docs/vision/08-roadmap.md)

## Diagnóstico honesto (jul-2026)

| Dimensión | Estado |
| --- | --- |
| Producto | **Fuerte** — plataforma completa + 3 capacidades IA con evals al 100% |
| Tecnología | **Fuerte** — arquitectura hexagonal, billing con enforcement, 14 crons |
| Tesis/secreto | **Fuerte** — cuadrante competitivo verificado vacío |
| **Distribución** | **DÉBIL — 0 usuarios, 0 canal probado. El riesgo #1** |
| Monetización | Media — pricing definido; falta recalcular economía de tokens y cobro anual |
| Equipo | Riesgo — bus factor 1 |

**Consecuencia:** el trabajo de la empresa en 2026 no es construir más producto; es **lanzar,
distribuir y aprender**. Este repo existe para operar exactamente eso.

## Principios operativos

1. **Power law en todo:** 1 nicho (intake operativo hispano), 1 canal dominante por ciclo,
   1 métrica norte (FAS), 1 diferenciador por ciclo de producto.
2. **Evals para el negocio:** cada apuesta (canal, campaña, plantilla, pricing) sale con
   hipótesis, métrica y kill criteria. Ciclo mensual: matar o doblar.
3. **Nada se adelanta de fase** sin cumplir el criterio de salida de la anterior.

## CORTO PLAZO — H2 2026: "Lanzar, aprender, no morir de silencio"

### Q3 2026 (ahora → sep)

1. **Gate de lanzamiento (ago):** cerrar bloqueantes legales (identidad del operador, buzones
   legal@/privacy@, DPAs), recalcular economía de tokens con precios reales Cerebras/OpenAI,
   matriz `LimitDialog` verificada, smoke E2E en verde. → seguimiento en
   [`00-core/operaciones/`](operaciones/estrategia.md).
2. **Lanzamiento público 24-ago-2026:** dominio público, onboarding pulido, disclosure AI Act.
3. **Distribución compuesta (ago–sep):** `llms.txt` + contenido agent-readable, 30+ plantillas
   como landings indexables, lanzamiento en comunidades hispanas, badge "Hecho con Formelia" con
   landing de conversión. → ejecución en [`03-growth/`](../03-growth/estrategia.md) y
   [`02-marketing/`](../02-marketing/estrategia.md).
4. **Aprendizaje:** dashboard de métricas norte, 20+ entrevistas de usuarios, instrumentar
   fuente de signup. → lo coordina el CEO desde core (el área de research se disolvió en la
   reestructuración del 2026-08-04).

**Criterio de salida:** ≥300 registros, activación ≥35%, share de creación con IA ≥30%, embudo
medido de punta a punta.

### Q4 2026 (oct–dic)

MCP server de Formelia (producto Y distribución) · API pública v0 + webhooks · cobro anual
(2 meses gratis) · display de moneda local · integración Google Sheets + Zapier · onda 2 de
plantillas (60+) y páginas por vertical · Sean Ellis test a los 100 activos.

**Criterio de salida:** ≥1.000 registros, ≥100 de pago, ≥40% signups orgánicos/AI-search,
retención M1 ≥40%, margen bruto IA medido ≥70%.

## MEDIANO PLAZO — 2027: "Diferenciar con lo que nadie puede copiar barato"

- **H1:** follow-ups adaptativos con IA, insights cross-formulario, moneda local transaccional,
  integraciones core (Slack, HubSpot, Make), programa de partners v1, primera contratación
  (growth/contenido ES) si el canal validó. Salida: $8–12K MRR, M3 ≥35%, Sean Ellis ≥40%,
  ≥15 agencias partner.
- **H2:** respuestas por voz asíncrona, verificación de humanidad v1, benchmarks v1 (red de
  datos), kit compliance AI Act, seed-readiness. Salida: $15–25K MRR, ≥50% signups orgánicos.

## LARGO PLAZO — 2028–2029: "De form builder a capa de datos estructurados"

- **2028:** payment forms con rails locales, vertical pack #1 ($99–299/mes), forms
  agent-readable, enterprise-lite, Intake OS v1.
- **2029:** voz realtime, red de benchmarks como producto, expansión pt-BR/Brasil, marketplace.
  **Norte: $100K+ MRR** y la posición de interfaz estándar humano-agente del mundo hispano.

## Secuencia de contratación (gates, no fechas)

| Gate | Rol |
| --- | --- |
| ≥500 signups/mes orgánicos | Growth/contenido ES |
| ~$5K MRR | Soporte/CS bilingüe (part-time → full) |
| Seed o ~$15K MRR | Ingeniero producto full-stack |
| 2027, con verticales | Founder-associate vertical (salud/educación) |

## Riesgos principales

| Riesgo | Mitigación |
| --- | --- |
| Distribución no despega (#1) | 3 canales compuestos en paralelo (AI-search, SEO, plantillas) con kill criteria mensuales; partners como plan B |
| WTP LATAM baja | Free generoso como cuña + monetizar agencias/verticales + cobro anual + USD España/US |
| Tally/Google cierran el gap ES | Velocidad + insights + WhatsApp + soporte nativo |
| Bus factor 1 | Docs/evals/runbooks + primera contratación técnica al gate |

## Historial de cambios

- 2026-07-30 — Documento inicial, sintetizado de docs/vision 07 y 08.
