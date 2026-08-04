# Estrategia de producto

> Documento vivo del equipo de Producto. Última actualización: 2026-08-04
> Área creada en la reestructuración del 2026-08-04. El código y la documentación técnica viven
> en [`../formelia-app`](../../formelia-app); aquí vive la definición de **qué construir y por
> qué**, subordinada a [`00-core/estrategia.md`](../00-core/estrategia.md) y al roadmap de
> [`../formelia-app/docs/vision/08-roadmap.md`](../../formelia-app/docs/vision/08-roadmap.md).

## Objetivo del área

Decidir qué se construye, para quién y en qué orden, y especificarlo con la claridad suficiente
para que arquitectura e implementación no adivinen. Producto responde al negocio: cada feature
debe poder explicar cómo mueve el FAS (Formularios Activos por Semana) o desbloquea un plan de
pago.

## Responsabilidades

0. **Roadmap:** el roadmap fechado de H2-2026 vive en [roadmap.md](roadmap.md) — es el
   documento operativo del área; se actualiza cada revisión mensual.
1. **PRDs:** toda feature significativa nace como PRD en [prds/](prds/README.md) antes de
   pasar a especificación técnica (`05-arquitectura/`).
2. **Priorización:** mantener el backlog ordenado por impacto en FAS y en la fecha de
   lanzamiento (15-ago-2026).
3. **UX:** flujos de usuario, decisiones de onboarding y de activación, siempre con las
   personas de core (Carolina, consultor multiplicador, respondedor móvil).
4. **Coordinar con research del mercado** los hallazgos de usuarios que cambien el roadmap
   (las entrevistas y su síntesis se gestionan desde core hasta nuevo aviso).

## Reglas innegociables

- Ninguna feature sin persona ni métrica de éxito declaradas.
- El anti-posicionamiento manda: no somos research, no somos chatbot, no somos no-code amplio.
- Español primero: ninguna feature sale si su experiencia en español se siente traducida.

## Historial de cambios

- 2026-08-04 — Versión inicial (área creada en la reestructuración).
