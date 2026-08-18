# Estrategia de marca y diseño

> Documento vivo del equipo de Marca. Última actualización: 2026-08-08
> Fuentes: [`docs/design/color-system.md`](../../../formelia-app/docs/design/color-system.md),
> [`docs/design/typography.md`](../../../formelia-app/docs/design/typography.md),
> [`00-core/posicionamiento.md`](../posicionamiento.md)

## Qué debe transmitir la marca

Formelia debe sentirse como **la herramienta profesional que por fin habla tu idioma**: cálida
pero seria, moderna sin ser fría, honesta sin ser aburrida. La comparación mental que buscamos:
*"se ve tan bien como Typeform, me trata tan claro como una conversación por WhatsApp y cuesta
lo que puedo pagar."*

Tres atributos, en orden:

1. **Confiable** — una PYME le va a entregar los datos de sus clientes. Nada de estética
   juguetona de startup; acabados premium, consistencia obsesiva.
2. **Cercana** — español nativo, tuteo, dolor nombrado antes que la solución. La marca habla
   como Carolina, no como un departamento legal.
3. **Distinta** — nos alejamos deliberadamente del azul corporativo SaaS (teal + crema) y del
   cliché IA (violeta + sparkles). Si un asset parece "otro SaaS más", está mal.

## Principios de diseño

1. **El protagonista es el formulario del cliente, no Formelia.** "Quien lo abre ve tu marca, no
   un formulario cualquiera." En piezas de marketing: mostrar la marca del cliente brillando, la
   nuestra acompañando.
2. **Teal como único acento de acción.** Éxito también es teal (no verde). El violeta solo existe
   como decorativo marginal, jamás asociado a IA.
3. **La IA no se disfraza de magia.** Sin sparkles, sin degradados morados, sin emoji de destello. La IA en
   Formelia es una herramienta seria que se muestra con resultados, no con fuegos artificiales.
4. **Cálido sobre clínico.** Warm cream como superficie antes que blanco puro; fotografía e
   ilustración con luz cálida.
5. **Legibilidad primero.** Lexend existe porque mejora velocidad de lectura. Toda pieza debe
   leerse bien en un móvil de gama media a pleno sol.

## Alcance del equipo

- Custodiar la [identidad visual](identidad-visual.md) y la [voz y tono](voz-y-tono.md).
- Producir y aprobar los assets de marca (logo, plantillas de piezas, portadas, OG images) en
  [`assets/`](assets/README.md).
- Revisar toda pieza pública antes de publicarse: checklist al final de este doc.
- Mantener coherencia entre producto (app), landing y redes: misma paleta, misma voz.

## Sistema de plantillas de piezas (por crear — prioridad ago-2026)

| Plantilla | Uso | Formato |
| --- | --- | --- |
| Post educativo (carrusel) | Instagram/LinkedIn | 1080×1350, teal sobre crema |
| Quote/insight | Instagram/X | 1080×1080 |
| Demo de producto (video corto) | TikTok/Reels/Shorts | 1080×1920, captions siempre |
| OG image de plantilla/landing | Blog/SEO | 1200×630 |
| Portada de plantilla pública | Galería de plantillas | según producto |

## Checklist de aprobación de cualquier pieza pública

- [ ] Usa la paleta oficial (teal/crema/grises; sin azul corporativo, sin violeta-IA).
- [ ] Tipografía: Lexend para titulares, Geist para cuerpo.
- [ ] Voz: tuteo, imperativo, frases cortas, sin jerga; ver [voz-y-tono.md](voz-y-tono.md).
- [ ] No infringe el anti-pitch (nada de "Typeform con IA", nada de promesas de agentes).
- [ ] Legible en móvil; contraste AA mínimo.
- [ ] CTA claro y honesto ("Crear formulario gratis") — sin coletillas comerciales
  (regla 5 de voz: informar, no vender).

## Deudas y pendientes de marca

- [ ] Unificar el copy del badge: "Hecho con Formelia" (builder) vs "Creado con Formelia"
  (footer). Decidir uno y sincronizar en producto.
- [ ] Corregir voseo residual en mensajes de error de insights ("Esperá", "Intentá") → tuteo.
- [ ] Exportar el logo a formatos de asset (SVG/PNG en tamaños) — hoy solo existe como
  componente React en el código.
- [ ] Definir plantillas maestras de piezas sociales (tabla de arriba).

## Historial de cambios

- 2026-08-08 — Regla de marca: **prohibido usar iconos y emoji** en el contenido que
  producimos (detalle en [voz-y-tono.md](voz-y-tono.md), regla 10). Barrido del repo: todos
  los pictogramas sustituidos por palabras.
- 2026-07-30 — Versión inicial.
