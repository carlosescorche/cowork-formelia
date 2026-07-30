# Legal

Seguimiento de compliance y asuntos legales. La revisión adversarial completa (26 hallazgos)
está en
[`docs/reports/legal-review-terms-privacy.md`](../../../formelia-app/docs/reports/legal-review-terms-privacy.md).

## Estructura

```
legal/
├── checklist-lanzamiento.md   Los 7 bloqueantes con estado y evidencia de cierre
├── entidad.md                 Decisión de entidad legal y jurisdicción (→ también como
│                              decisión de CEO en 00-core/decisiones/)
└── proveedores-dpa.md         Estado de DPAs y subencargados por proveedor
```

## Bloqueantes de lanzamiento (fecha límite 31-jul-2026)

| # | Ítem | Estado |
| --- | --- | --- |
| 1 | Nombre legal + domicilio del operador | ⬜ |
| 2 | Ley aplicable y foro en términos | ⬜ |
| 3 | Buzones `legal@` y `privacy@` | ⬜ |
| 4 | DPA propia + DPA OpenAI + verificación Cerebras | ⬜ |
| 5 | Redis nombrado en subencargados | ⬜ |
| 6 | Agente DMCA registrado | ⬜ |
| 7 | Disclosure AI Act (vigente 02-ago) | ⬜ |

**Regla:** cada ítem se cierra con evidencia (link o documento) — no con "ya casi". Al cerrar
los 7, actualizar [`00-core/memoria.md`](../../00-core/memoria.md).

## Vigilancia continua

- AI Act: obligaciones aplicables a superficies conversacionales y disclosure.
- Privacidad LATAM: leyes de datos de MX/CO/AR/CL cuando entremos con moneda local.
- Los legales del producto (términos/privacidad ES+EN) prevalecen en español — mantener esa
  regla en toda actualización.
