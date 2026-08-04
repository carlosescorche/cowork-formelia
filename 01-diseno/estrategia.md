# Estrategia de diseño

> Documento vivo del equipo de Diseño. Última actualización: 2026-08-04
> Área creada en la reestructuración del 2026-08-04. La identidad de marca (colores, tipografía,
> voz y tono) **no vive aquí**: es fuente de verdad en [`00-core/marca/`](../00-core/marca/).
> Este equipo la ejecuta.

## Objetivo del área

Producir todo lo visual que Formelia muestra al mundo — piezas de redes, plantillas, OG images,
assets de landing, exports de logo — con calidad consistente y fiel a la marca definida en core.
Diseño es el puente entre los briefs (de marketing y otras áreas) y el arte final.

## Responsabilidades

1. **Producción de piezas:** convertir briefs en artes finales (estáticos y video) aplicando
   [`00-core/marca/identidad-visual.md`](../00-core/marca/identidad-visual.md).
2. **Dirección de arte por pieza (no plantillas fijas):** el feed no repite layouts — cada
   pieza lleva concepto, referencia y prompt propios, generados con el stack AI (Higgsfield /
   HeyGen vía MCP) en 2–3 variantes para elección del founder. La coherencia viene del
   **sistema visual** (paleta, tipografía, tono fotográfico), no de la repetición. Las
   plantillas-código (HTML/CSS en `assets/plantillas/`) quedan solo para assets funcionales
   seriados: OG images, portadas de blog.
3. **Assets de marca:** exports de logo, iconografía y recursos compartidos, versionados en
   [assets/](assets/README.md).
4. **Auditoría visual:** revisar coherencia entre producto, landing y redes; las discrepancias
   con la fuente canónica (`../formelia-app/docs/design/`) se reportan, no se improvisan.

## Reglas innegociables (resumen — detalle en `00-core/marca/`)

- Teal `#00786f` único acento de acción; éxito = teal, nunca verde.
- IA sin violeta ni sparkles: grises neutros, iconos funcionales.
- Lexend (títulos) + Geist (cuerpo). Screenshots reales, nunca UI inventada.

## Historial de cambios

- 2026-08-04 — Versión inicial (área creada al separar ejecución de diseño de la definición de
  marca, que pasa a `00-core/marca/`).
