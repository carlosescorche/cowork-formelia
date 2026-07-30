# Estrategia de operaciones

> Documento vivo del equipo de Operaciones (legal, finanzas, administración).
> Última actualización: 2026-07-30

## Objetivo del área

Que la empresa pueda lanzar, cobrar y crecer **sin sustos**: compliance en verde, números
claros, y los riesgos operativos (bus factor, proveedores, caja) vigilados. Operaciones es el
área que convierte "proyecto de founder" en "empresa que puede recibir clientes e inversión".

## Frente legal ([legal/](legal/README.md)) — CRÍTICO AHORA

Bloqueantes de lanzamiento identificados en la revisión legal adversarial
([`docs/reports/legal-review-terms-privacy.md`](../../formelia-app/docs/reports/legal-review-terms-privacy.md)),
con fecha límite **31-jul-2026**:

1. [ ] Identificar al operador: nombre legal + domicilio (decisión de entidad/jurisdicción).
2. [ ] Fijar ley aplicable y foro en los términos.
3. [ ] Crear buzones `legal@formelia.com` y `privacy@formelia.com`.
4. [ ] Plantilla de DPA propia; aceptar DPA de OpenAI; verificar no-entrenamiento de Cerebras.
5. [ ] Nombrar el proveedor de Redis en la lista de subencargados.
6. [ ] Registrar agente DMCA.
7. [ ] Disclosure AI Act en superficies conversacionales (vigente **02-ago-2026**).

## Frente finanzas ([finanzas/](finanzas/README.md))

- **Economía unitaria de IA (bloqueante):** recalcular costo por token con precios reales de
  Cerebras/OpenAI (el PRD de billing razona con un proveedor obsoleto). Validar margen bruto
  IA ≥70% por plan con telemetría real. Riesgo actual: vender a pérdida sin saberlo.
- **Guardarraíles ya construidos (verificar, no construir):** enforcement en 3 capas,
  kill-switch por env, circuit breaker de $500/mes en concesión de cuotas gratis.
- **Cobro anual (2 meses gratis) en Q4-2026** — mejora caja y retención; table stake pendiente.
- **Registro mensual:** MRR, costos de infraestructura y de IA, burn, runway. Sin contabilidad
  sofisticada todavía: una tabla honesta al mes.
- Pagos vía **Polar.sh como merchant of record** (impuestos del checkout resueltos por ellos —
  ventaja operativa deliberada).

## Frente administración y riesgo operativo

- **Bus factor 1:** mitigación por documentación (fuerte), evals como red de seguridad, y
  runbooks de operación (crons, billing, incidentes) — mantener al día en `formelia-app`.
- **Proveedores críticos:** Vercel, Supabase, Redis (¿proveedor?), Cerebras, OpenAI, Polar,
  Resend. Mantener lista con: contrato/plan, costo mensual, riesgo de dependencia, plan B.
- **Contrataciones:** operaciones prepara lo administrativo cuando un gate de contratación se
  acerque (ver [secuencia en core](../00-core/estrategia.md#secuencia-de-contratación-gates-no-fechas)).

## Cadencia

- **Semanal (pre-lanzamiento):** revisar checklist legal hasta cerrarlo.
- **Mensual (día 1):** cerrar números del mes en `finanzas/`, actualizar
  [`00-core/metricas.md`](../00-core/metricas.md) (tablero mensual).
- **Trimestral:** revisión de proveedores y riesgos.

## Historial de cambios

- 2026-07-30 — Versión inicial.
