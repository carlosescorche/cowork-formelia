# Identidad visual

> Última actualización: 2026-07-30 · Fuente canónica:
> [`docs/design/color-system.md`](../../../formelia-app/docs/design/color-system.md) y
> [`docs/design/typography.md`](../../../formelia-app/docs/design/typography.md)

## Filosofía

*"Los colores de Formelia provienen de la naturaleza, refinados para aplicaciones digitales
premium. Esta paleta se aleja intencionalmente del azul corporativo típico de herramientas SaaS,
creando una identidad distintiva y memorable."*

## Paleta

### Forest Teal (primario)

| Tono | Hex | Uso |
| --- | --- | --- |
| 50 | `#e8f7f7` | Fondos suaves |
| 100 | `#d1eeee` | Fondos hover |
| 300 | `#5fc9c9` | Acentos secundarios |
| 400 | `#00d5be` | Highlights |
| 500 | `#159999` | Éxito (no verde) |
| **700** | **`#00786f`** | **Primario semántico — CTAs, enlaces, acento de acción** |
| 900 | `#0a4d4d` | Wordmark, titulares oscuros |
| 950 | `#022f2e` | Fondos oscuros |

### Warm Cream (superficies cálidas)

`50 #f8f5f0` · `100 #f0eae0` · `200 #e5ded0` · `300 #d4c9b8` · `500 #b5a288` · `700 #7d6d58` ·
`900 #3d3428`. Usar como fondo de shell, piezas y slides en lugar de blanco puro.

### Grises

`50 #f9f9f9` · `100 #f2f2f2` · `200 #e5e5e5` · `400 #b8b8b8` · `600 #6b6b6b` · `800 #383838` ·
`950 #1a1a1a`. Negro de texto: `#0d0d0d`.

### Semánticos y terceros

Error/coral `#fa4444` · Warning `#f59e0b` · Danger `#dc2626` · Éxito = teal-500 ·
WhatsApp `#25d366` · LinkedIn `#0a66c2` · Premium/corona `#ffb347`.

## Reglas de color innegociables

1. El acento de acción es **siempre teal**. Un solo acento por pieza.
2. **Éxito = teal, nunca verde** (coherencia de marca).
3. **La IA nunca usa violeta ni iconos Sparkles.** Se representa con grises neutros e iconos
   funcionales (bombilla, documento, pluma). Decisión anti-cliché deliberada.
4. Sin azul corporativo. Si una pieza podría ser de cualquier SaaS, rehacerla.

## Tipografía

| Familia | Uso | Pesos |
| --- | --- | --- |
| **Lexend** | Branding, wordmark, titulares H1–H4, display | 400–800 |
| **Geist** | Cuerpo, UI, H5–H6, navegación | 100–700 |
| Geist Mono | Solo interfaces técnicas | — |

Escala display: XL 72px Bold · L 56px Bold · M 48px SemiBold. Base de cuerpo: 16px.
Lexend se eligió por diseño científico para velocidad de lectura: la legibilidad ES la marca.

## Logo

- Icono SVG `FormeliaIcon` + wordmark "Formelia" en Lexend Medium, tracking-tight,
  color teal-900 (`#0a4d4d`). Color canónico del icono: `#0f766e`.
- Variantes: `full` / `icon` / `text`. Fuente actual: componente
  `src/components/common/Logo/Logo.tsx` en `formelia-app`.
- **Pendiente:** exportar a assets estáticos (SVG + PNG @1x/@2x, claro/oscuro) en
  [`assets/`](assets/README.md).

## Aplicación en piezas de marketing

- Fondo preferido: crema 50/100 o teal 950 (modo oscuro de marca).
- Titular: Lexend SemiBold/Bold en teal-900 (sobre claro) o crema 50 (sobre oscuro).
- CTA/acento: teal-700. Un solo acento por pieza.
- Screenshots de producto: siempre reales, nunca mockups inventados que muestren UI que no
  existe.
- El QR y el badge "Hecho con Formelia" son elementos de marca: tratarlos con el mismo cuidado.
