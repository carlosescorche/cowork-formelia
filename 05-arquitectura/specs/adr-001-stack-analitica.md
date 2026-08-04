# ADR-001 — Stack de analítica y atribución

- **Fecha:** 2026-08-04
- **Estado:** Vigente
- **Contexto de negocio:** [estrategia H2-2026](../../00-core/decisiones/2026-08-04-estrategia-h2-2026.md) ·
  prerrequisito del roadmap (05–08 ago): "sin atribución ningún experimento es interpretable"

## Decisión

**Tres capas, cada una con su dueño:**

1. **PostHog Cloud EU (free tier)** como herramienta única de analítica web + producto:
   visitas, referrers, UTMs, embudos, sesiones. Instalado con proxy first-party (rewrite
   `/ingest` en Next.js para que los bloqueadores no lo maten), en modo respetuoso de
   privacidad (sin cookies de terceros; EU hosting).
2. **Atribución first-party propia en Supabase** (no depende de PostHog): en la primera
   visita se capturan `utm_source/medium/campaign`, `referrer` y `landing_page`, se persisten
   (first-touch, 30 días) y al registrarse se escriben en el perfil del usuario. La fuente de
   cada signup vive en NUESTRA base de datos.
3. **La verdad de negocio se calcula desde Supabase:** FAS, activación, conversión, MRR salen
   de queries sobre nuestros datos (formularios, respuestas, billing). PostHog explica el
   comportamiento; no es la fuente de verdad.

**Reparto con lo ya decidido:** Metricool mide las redes (alcance, CTR por pieza); PostHog
mide el sitio y el producto; Supabase guarda la atribución y las métricas norte.

## Eventos mínimos (v1)

| Evento | Propiedades clave |
| --- | --- |
| `$pageview` (auto) | path, referrer, UTMs |
| `signup` | source, medium, campaign, referrer, landing_page |
| `form_created` | method: `ia` \| `manual` \| `plantilla` (+ template_slug) |
| `form_published` | form_id, time_to_publish |
| `response_received` | form_id (para FAS) |
| `upgrade` | plan |

`identify` tras signup para unir el anónimo pre-registro con el usuario.

## Alternativas consideradas

1. **GA4** — gratis, pero exige banner de consentimiento (fricción exactamente donde medimos
   conversión), es complejo de operar y manda datos a Google. Descartado.
2. **Plausible / Fathom (~$9–15/mes)** — excelentes para web, pero solo web: sin embudos de
   producto ni identify. Habría que sumar una segunda herramienta igual.
3. **Vercel Analytics** — superficial (pageviews), sin embudos ni eventos identificados.
4. **Mixpanel / Amplitude** — potentes en producto pero débiles en web analytics; PostHog
   cubre ambos con un solo DPA y un solo SDK.
5. **Umami self-hosted** — gratis pero es infra que mantener con 3h/día. No.
6. **App + base de datos separadas para marketing/blog/atribución** (propuesta del founder,
   evaluada 2026-08-04) — descartada por ahora: lo voluminoso ya vive fuera (eventos →
   PostHog), el blog son archivos MDX sin base, las plantillas son producto por naturaleza, y
   la atribución son 6 columnas cuyo valor es precisamente el JOIN con activación/pago en la
   misma base (el corte de avatares del 30-sep es ese JOIN). Una segunda app duplica deploys,
   migraciones y superficie de fallo para un bus factor 1.
   **Gate de revisión — se separa cuando ocurra cualquiera de estas:** marketing necesita CMS
   con editor · hay una contratación dueña del sitio de marketing · las tablas de marketing
   crecen más allá de la atribución (secuencias de email, lead scoring). Mientras tanto:
   futuras tablas de marketing nacen en un schema `marketing` separado, y rige la regla de
   dependencia — el core nunca depende de marketing; marketing solo lee del core.

## Consecuencias

- **Implementación en formelia-app (05–08 ago):** SDK `posthog-js` + proxy `/ingest`,
  captura de UTMs (middleware/cliente), migración con columnas de atribución en el perfil
  (`signup_source`, `signup_medium`, `signup_campaign`, `signup_referrer`,
  `signup_landing_page`, `first_seen_at`), instrumentación de los 6 eventos, `identify`.
- **Legal:** PostHog entra al inventario de subencargados (política de privacidad + DPA) —
  debe cerrarse junto con los ítems 4–5 del checklist de lanzamiento, antes del 15-ago.
- **Dashboards iniciales:** embudo registro → publicado · signups por `utm_campaign`
  (= por avatar) · tráfico por página de plantilla. Con esto el informe semanal del viernes
  y el corte de avatares del 30-sep son medibles.
- **Costo:** $0 (free tier: 1M eventos/mes — años de margen a nuestra escala).
- **Riesgo aceptado:** dependencia de un tercero con free tier. Mitigado: la atribución vive
  en Supabase (first-party) y PostHog es reemplazable u auto-hosteable sin perder historia de
  negocio.
