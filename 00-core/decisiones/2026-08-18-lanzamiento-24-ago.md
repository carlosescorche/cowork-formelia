# El lanzamiento público se mueve al 24-ago-2026

- **Fecha:** 2026-08-18 (registro a posteriori; el cambio ya estaba ejecutado en
  [`estrategia.md`](../estrategia.md))
- **Estado:** Vigente
- **Área(s) afectada(s):** core, marketing, growth

## Contexto

El lanzamiento estaba fijado para el 15-ago-2026 con el criterio "se lanza con lo que haya"
(estado del 04-ago en [`memoria.md`](../memoria.md)). La fecha llegó con trabajo de
lanzamiento aún abierto: la landing de conversión se commiteó el 14-ago con dos tareas
pendientes (publicar un formulario demo real y convertir el hero en campo de prompt), las
bios de redes y el teaser sembrado seguían con el orden viejo del headline
([decisión del 14-ago](2026-08-14-headline-promesa.md)), y las piezas de video del
lanzamiento (los dos reels del 16-ago) estaban todavía en producción el 17-ago.

El cambio se ejecutó primero en `00-core/estrategia.md` (gate de lanzamiento movido a
agosto, fecha pública al 24-ago) sin registro de decisión ni propagación: el resto de
documentos siguió diciendo 15-ago. Este registro formaliza la decisión y acompaña la
propagación de la fecha.

## Decisión

El lanzamiento público pasa del 15-ago-2026 al **24-ago-2026**. El gate de bloqueantes
(legal, economía de tokens, `LimitDialog`, smoke E2E) se cierra en agosto, antes de esa
fecha. La ventana de lanzamiento de la campaña se desplaza una semana (24–31 ago); la
consolidación sigue hasta el 30-sep.

## Alternativas consideradas

No quedaron registradas: la decisión se documenta a posteriori, cuando la fecha original ya
había pasado sin lanzamiento. La alternativa implícita — lanzar el 15-ago con la landing sin
demo real y las piezas de video a medias — se descartó con los hechos.

## Consecuencias

- Documentos actualizados al 24-ago: `CLAUDE.md`, `README.md`, `00-core/memoria.md`,
  `00-core/marca/assets/README.md`, `00-core/operaciones/legal/README.md`,
  `02-marketing/estrategia.md`, `02-marketing/campanas/README.md`,
  `03-growth/estrategia.md`, `.claude/skills/instagram/SKILL.md`.
- Las menciones al 15-ago en registros históricos (movimientos de memoria, decisión del
  14-ago) se conservan: eran ciertas cuando se escribieron.
- Riesgo aceptado: nueve días más sin audiencia ni canal probado, con distribución como
  riesgo #1 declarado.

## Criterio de revisión

Si el 24-ago llega sin los pendientes de la landing cerrados, un nuevo aplazamiento no se
ejecuta en silencio: se registra con causa y nueva fecha antes de tocar `estrategia.md`.
