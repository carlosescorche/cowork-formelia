# Assets de marca

Repositorio de archivos de marca aprobados. Solo entra aquí lo que pasó el checklist de
[estrategia.md](../estrategia.md).

## Estructura esperada

```
assets/
├── logo/            SVG y PNG del logo (full/icon/text, claro/oscuro, @1x/@2x)
├── plantillas/      Plantillas maestras de piezas (carrusel, quote, video, OG)
├── screenshots/     Capturas oficiales del producto, actualizadas por versión
└── og/              Imágenes OG/social por página o campaña
```

## Convenciones

- Nombres: `formelia-logo-full-dark.svg`, `og-plantilla-inscripcion-curso.png`,
  `screenshot-insights-2026-08.png` (con fecha si caduca con versiones del producto).
- Los screenshots se regeneran cuando cambia la UI: nunca publicar capturas de UI vieja.
- Fuente del logo: componente `Logo.tsx` en `formelia-app` — al exportar, verificar color
  canónico (`#0f766e` icono, `#0a4d4d` wordmark).

## Pendientes

- [ ] Exportar set completo de logos desde el componente React.
- [ ] Crear las 5 plantillas maestras definidas en la estrategia de marca.
- [ ] Set de screenshots oficiales del producto para el lanzamiento (15-ago-2026).
