# Estrategia de growth (distribución)

> Documento vivo del equipo de Growth. Última actualización: 2026-07-30
> Fuente: [`docs/vision/07-plan-transformacion-10x.md`](../../formelia-app/docs/vision/07-plan-transformacion-10x.md) §3
> **Este es el trabajo #1 de la empresa post-lanzamiento.** Distribución es el riesgo #1: 0
> usuarios, 0 canal probado.

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
6. **Comunidades hispanas** — canal de lanzamiento (ejecuta
   [comunicación](../03-comunicacion/comunidad/README.md); growth mide conversión por
   comunidad).
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

- Fuente de signup instrumentada (UTM + referrer) — verificar antes del 15-ago.
- Dashboard de métricas norte: FAS, activación, T2F, share IA, conversión — revisar semanal.
- El punto de fuga que más importa al inicio: registro → primer form **publicado**.

## Prioridades ago–sep 2026 (con el lanzamiento)

1. [ ] Verificar instrumentación de fuente de signup + UTMs (pre-15-ago).
2. [ ] `llms.txt` + contenido agent-readable en el sitio (pre-15-ago).
3. [ ] Sembrar Formelia en 10+ directorios de herramientas que los LLMs citan (ago).
4. [ ] Onda 1 de plantillas-landing: 30+ por JTBD/país (ago–sep).
5. [ ] Landing del badge "Hecho con Formelia" con creación instantánea (sep).
6. [ ] Primer informe mensual de canales (01-sep): matar o doblar.

## Kill criteria por canal (iniciales — ajustar con datos)

| Canal | Señal de vida a 8 semanas | Si no llega |
| --- | --- | --- |
| AI-search/directorios | Primeros referrals medibles de LLMs/directorios | Revisar dónde estamos listados, no matar (compounding lento) |
| SEO/blog | Impresiones crecientes en keywords objetivo | Revisar keywords, no matar antes de 6 meses |
| Plantillas | ≥10% de signups desde páginas de plantilla | Rehacer las 10 con más tráfico |
| Comunidades | ≥50 registros atribuibles al lanzamiento | No repetir formato; pasar a relaciones 1:1 |
| Badge | CTR medible + primeros signups | Iterar landing del badge |

## Historial de cambios

- 2026-07-30 — Versión inicial.
