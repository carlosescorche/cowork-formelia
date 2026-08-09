# Roadmap de producto — H2 2026

> Última actualización: 2026-08-04 · Decisión:
> [estrategia H2-2026](../00-core/decisiones/2026-08-04-estrategia-h2-2026.md)
> Presupuesto real: **~5h/semana** (30% del tiempo del founder). Regla de entrada: nada se
> construye si no mueve el FAS o desbloquea distribución. Toda feature declara su métrica
> antes de construirse (mini-PRD en [prds/](prds/README.md) para lo significativo).

## Agosto — lanzar y medir

| Fechas | Entregable | Métrica que mueve | Estado |
| --- | --- | --- | --- |
| 04–05 ago | **Auditoría de bloqueantes** del gate de julio (legal, economía de tokens, LimitDialog, disclosure AI Act) con evidencia por ítem | Riesgo de lanzamiento | pendiente |
| 05–08 ago | **Instrumentación de atribución** ([ADR-001](../05-arquitectura/specs/adr-001-stack-analitica.md)): PostHog EU + proxy first-party + UTMs escritos en Supabase al signup + 6 eventos base | Sin esto ningún experimento es interpretable | pendiente |
| 06–08 ago | **`llms.txt`** + verificación robots/sitemap | AI-search (canal #1) | pendiente |
| 08–14 ago | **12 plantillas públicas** (3 por avatar) como landings indexables con CTA "Usar esta plantilla" | Plantillas-SEO + onboarding instantáneo | pendiente |
| 11–14 ago | Smoke E2E del onboarding móvil (crear → publicar → responder) + landing del badge si falta | Activación | pendiente |
| **15 ago** | **LANZAMIENTO PÚBLICO** | — | pendiente |
| 16–31 ago | **`/blog` en formelia.io** (MDX) + 4 artículos fundacionales (1 por avatar) | SEO/AI-search | pendiente |
| 16–31 ago | Fricción de onboarding según feedback real de los primeros usuarios | Activación (registro → publicado) | pendiente |

## Septiembre — activación y conversión

- **Plantillas → 30+** (2–3/semana, priorizadas por los avatares con más tracción).
- **Precios en moneda local** (display MXN/COP) — foco México+Colombia decidido.
- **Newsletter quincenal** (Resend) para retener signups que no activaron.
- **Sean Ellis test** al llegar a 100 usuarios activos.

## Octubre — monetización

- **Cobro anual** (2 meses gratis).
- **Integración Google Sheets** — el puente desde el statu quo de Carolina (Forms+Sheets).

## Noviembre — plataforma y AI-search

- **API pública v0 + webhooks.**
- **MCP server v0** — producto Y distribución (ser la respuesta operativa de los LLMs).

## Diciembre — consolidar

- Plantillas 60+ · hardening · revisión trimestral y foco 2027 (contra criterio de salida Q4:
  ≥1.000 registros, ≥100 de pago, ≥40% orgánico, M1 ≥40%, margen IA ≥70% medido).

## Qué NO entra en H2 (guardarraíl)

Follow-ups adaptativos, voz asíncrona, benchmarks, verticales pack, enterprise — todo eso es
2027+ según `00-core/estrategia.md`. Nada se adelanta de fase.

## Historial de cambios

- 2026-08-04 — Versión inicial (sesión de estrategia H2).
