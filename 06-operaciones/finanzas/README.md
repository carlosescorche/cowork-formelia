# Finanzas

Números de la empresa. Sin sofisticación prematura: una verdad honesta al mes.

## Estructura

```
finanzas/
├── economia-ia.md      Modelo de costos de IA por plan (bloqueante: recalcular con precios
│                       reales Cerebras/OpenAI y validar margen ≥70%)
├── cierres/            Cierre mensual: AAAA-MM.md (MRR, costos, burn, runway, notas)
└── proveedores.md      Lista de proveedores: plan, costo mensual, riesgo, plan B
```

## Cierre mensual (plantilla para `cierres/AAAA-MM.md`)

| Concepto | Valor |
| --- | --- |
| MRR (Polar) | |
| Clientes de pago (Pro / Team) | |
| Costo IA del mes (Cerebras + OpenAI) | |
| Costo infra (Vercel, Supabase, Redis, Resend) | |
| Margen bruto IA | (target ≥70%) |
| Burn neto | |
| Runway | |
| Nota del mes | 1–3 frases honestas |

## Reglas

1. El margen de IA se calcula con telemetría real (`ai_generation_log`), no con estimaciones.
2. Ninguna feature de IA sale sin costo unitario medido y cubierto por el plan que la incluye
   (regla de margen del doc 07).
3. Los datos del cierre alimentan el tablero de [`00-core/metricas.md`](../../00-core/metricas.md).

## Pendiente crítico (agosto 2026)

- [ ] `economia-ia.md` con precios reales por token de Cerebras y OpenAI, costo por crédito
  (1 crédito = 1.000 tokens) y margen por plan (Free 500 / Pro 2.500 / Team 4.500 créditos
  efectivos al mes). Decide si el pricing actual es sostenible ANTES de escalar adquisición.
