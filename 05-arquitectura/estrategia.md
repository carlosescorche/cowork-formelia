# Estrategia de arquitectura

> Documento vivo del equipo de Arquitectura. Última actualización: 2026-08-04
> Área creada en la reestructuración del 2026-08-04. El código y su documentación viven en
> [`../formelia-app`](../../formelia-app); aquí viven las **decisiones técnicas y
> especificaciones** que traducen los PRDs de [`04-producto/`](../04-producto/estrategia.md)
> en cómo construir.

## Objetivo del área

Que cada feature tenga un camino técnico decidido antes de escribir código: trade-offs
evaluados, seguridad y performance consideradas, y la decisión registrada para no re-discutirla.

## Responsabilidades

1. **Specs técnicos:** todo PRD aprobado recibe su especificación en [specs/](specs/README.md)
   (modelo de datos, APIs, caché, RLS, diagramas) antes de implementarse.
2. **Decisiones técnicas (ADRs):** las decisiones de arquitectura con consecuencias duraderas
   se registran en specs/ como ADR; las que afectan al negocio (costos, proveedores, riesgo)
   se elevan además a [`00-core/decisiones/`](../00-core/decisiones/).
3. **Seguridad y performance:** revisar políticas RLS, superficies de datos personales
   (relevante para compliance — coordina con `00-core/operaciones/legal/`) y presupuestos de
   latencia/costo de IA.
4. **Deuda técnica:** mantener visible la deuda que amenaza el lanzamiento o el margen.

## Reglas innegociables

- Ninguna feature con datos de usuarios sale sin revisión de RLS y privacidad.
- El costo de IA por operación se estima en el spec, antes de construir (el margen ≥70% es
  restricción de negocio, ver `00-core/operaciones/`).
- Decisión no registrada = decisión que se va a re-discutir. Todo ADR con fecha y contexto.

## Historial de cambios

- 2026-08-04 — Versión inicial (área creada en la reestructuración).
