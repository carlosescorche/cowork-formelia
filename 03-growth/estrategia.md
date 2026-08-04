# Estrategia de growth (distribución)

> Documento vivo del equipo de Growth. Última actualización: 2026-08-04
> Fuente: [`docs/vision/07-plan-transformacion-10x.md`](../../formelia-app/docs/vision/07-plan-transformacion-10x.md) §3
> **Este es el trabajo #1 de la empresa post-lanzamiento.** Distribución es el riesgo #1: 0
> usuarios, 0 canal probado.

## Estado y foco (2026-08-04)

- **Soft launch abierto** (cualquiera puede registrarse) sin anuncio. Lanzamiento público
  **fijo el 15-ago**. Audiencia previa: cero. Founder: ~10h/sem para distribución.
- **País foco:** México + Colombia (comunidades, keywords, horarios, ejemplos).
- **Avatares:** 4 en test con corte a 2 el 30-sep — [`02-marketing/avatares.md`](../02-marketing/avatares.md);
  growth mide su atribución. Decisión:
  [estrategia H2-2026](../00-core/decisiones/2026-08-04-estrategia-h2-2026.md).

## Objetivo del área

Encontrar y componer los canales que llevan a Formelia de 0 → 1.000 registros (Q4 2026) → señal
de PMF. Growth posee: signups/mes por canal, activación, conversión free→pago, CTR del badge.
Marketing posee el mensaje; growth posee el sistema que lo distribuye y mide.

## Los 7 canales, en orden de prioridad (impacto compuesto × timing)

1. **AI-search / LLM referrals** — el canal que más crece y el más barato de ganar temprano.
   `llms.txt`, contenido estructurado para AI Overviews, MCP server público (Q4), presencia en
   directorios que los LLMs citan. Tally ya vive de esto (ChatGPT = su canal #1). En español,
   la competencia por ser "la respuesta del LLM" es casi nula. **Nuestra asimetría.**
2. **SEO español de intención operativa** — keywords de job-to-be-done por país, no "form
   builder". Ejecuta marketing ([blog-seo](../02-marketing/blog-seo/README.md)); growth define
   keywords y mide.
3. **Galería de plantillas por vertical/país** — cada plantilla es una landing indexable Y un
   onboarding instantáneo (clonar → publicar). Meta Q3: 30+; Q4: 60+.
4. **Loop viral "Hecho con Formelia"** — badge forzado en Free (ya implementado). Optimizar el
   CTR del badge con una landing de aterrizaje que permita crear al instante.
5. **Consultores/agencias multiplicadores** — programa de partners v1 en Q1-2027; mientras
   tanto, identificar y cuidar a mano a los primeros ([partners/](partners/README.md)).
6. **Comunidades hispanas** — canal de lanzamiento (desde la reestructuración del 2026-08-04
   la ejecución de comunidades es de growth; growth también mide conversión por comunidad).
7. **Pagado** — SOLO después de PMF y con payback <3 meses medido. Hasta entonces, $0 en ads.

**Regla power law:** un canal dominante por ciclo. Q3–Q4 2026: los canales 1–3 en paralelo
controlado con kill criteria mensuales; 4 y 6 como apoyo puntual.

## Sistema de experimentos

Todo lo que hace growth es un experimento con hipótesis, métrica y kill criteria — "evals para
el negocio". Registro en [experimentos/](experimentos/README.md) usando el
[TEMPLATE](experimentos/TEMPLATE.md). Ciclo mensual: **matar o doblar**, sin apego.

## Embudo y su instrumentación

```
Descubrimiento → Visita landing → Registro → Crea form → Publica → Recibe 5 respuestas (FAS)
                                     ↓ ≥45% en 7 días (activación)          → Convierte a pago
```

- Fuente de signup instrumentada (UTM + referrer) — verificar antes del 15-ago. Stack
  decidido en [ADR-001](../05-arquitectura/specs/adr-001-stack-analitica.md): PostHog EU
  (web + producto) + atribución first-party en Supabase; Metricool mide las redes.
- Dashboard de métricas norte: FAS, activación, T2F, share IA, conversión — se calculan desde
  Supabase (fuente de verdad); revisión semanal (viernes) con informe generado por Claude.
- El punto de fuga que más importa al inicio: registro → primer form **publicado**.

## Prioridades ago–sep 2026 (con el lanzamiento)

1. [ ] Verificar instrumentación de fuente de signup + UTMs (05–08 ago — **prerrequisito de
   todo lo demás**).
2. [ ] `llms.txt` + contenido agent-readable en el sitio (06–08 ago).
3. [ ] **Comunidades MX/CO:** identificar 5 (grupos de FB/WhatsApp/Slack de emprendedores,
   consultores, psicólogos, coordinadores académicos) y empezar a aportar valor YA (desde
   04-ago, 30 min/día) — se pide/anuncia recién el 15-ago. Medir con UTM por comunidad.
4. [ ] Onda 1 de plantillas-landing: 12 pre-lanzamiento (3 por avatar) → 30+ a fin de sep.
5. [ ] Sembrar Formelia en 10+ directorios de herramientas que los LLMs citan (ago).
6. [ ] **Outreach artesanal LinkedIn:** 10 contactos/sem del avatar en rotación (desde
   11-ago, empieza con consultoras). Mensaje 1:1 genuino con demo personalizada — nunca spam.
   Meta a 4 semanas: ≥3 llamadas, 1 caso de estudio.
7. [ ] Landing del badge "Hecho con Formelia" con creación instantánea (sep).
8. [ ] Primer informe mensual de canales (01-sep): matar o doblar.

## Kill criteria por canal (iniciales — ajustar con datos)

| Canal | Señal de vida a 8 semanas | Si no llega |
| --- | --- | --- |
| AI-search/directorios | Primeros referrals medibles de LLMs/directorios | Revisar dónde estamos listados, no matar (compounding lento) |
| SEO/blog | Impresiones crecientes en keywords objetivo | Revisar keywords, no matar antes de 6 meses |
| Plantillas | ≥10% de signups desde páginas de plantilla | Rehacer las 10 con más tráfico |
| Comunidades | ≥50 registros atribuibles al lanzamiento | No repetir formato; pasar a relaciones 1:1 |
| Badge | CTR medible + primeros signups | Iterar landing del badge |
| Outreach LinkedIn | ≥3 llamadas por cada 40 contactos | Cambiar avatar o mensaje; si nada, matar |

## Historial de cambios

- 2026-08-04 — Estado y foco actualizados (soft launch, MX+CO, avatares con corte);
  comunidades y outreach entran a prioridades con fechas.
- 2026-07-30 — Versión inicial.
