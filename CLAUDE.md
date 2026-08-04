# CLAUDE.md — Formelia HQ

Este repo es el entorno de gestión de Formelia como empresa. No contiene código de producto:
el producto vive en `../formelia-app`.

Áreas (desde la reestructuración del 2026-08-04): `00-core/` (dirección — incluye `marca/` y
`operaciones/`), `01-diseno/`, `02-marketing/`, `03-growth/`, `04-producto/`,
`05-arquitectura/`.

## Reglas de trabajo

1. **Jerarquía de verdad:** `00-core/` manda. Antes de producir cualquier cosa para un área, lee
   su `estrategia.md` y verifica que no contradiga `00-core/posicionamiento.md` ni
   `00-core/estrategia.md`. La investigación profunda de respaldo está en
   `../formelia-app/docs/vision/` (docs 01–10).
2. **Cada área trabaja en su carpeta.** El trabajo producido (piezas, briefs, informes) se guarda
   en las subcarpetas del área siguiendo las convenciones de nombrado de su README. Nunca sueltes
   archivos en la raíz.
3. **Decisiones del CEO → `00-core/decisiones/`.** Cualquier decisión estratégica (pricing,
   posicionamiento, canal, contratación, pivote) se registra con el TEMPLATE antes o
   inmediatamente después de ejecutarla. Formato de nombre: `AAAA-MM-DD-slug.md`.
4. **Memoria viva → `00-core/memoria.md`.** Al cerrar una sesión de trabajo significativa,
   actualiza la sección "Estado actual" y "Últimos movimientos" con fecha. Es el archivo que
   cualquier sesión futura lee primero para retomar contexto.
5. **Documentos vivos con fecha.** Toda `estrategia.md` lleva `Última actualización: AAAA-MM-DD`
   al inicio. Al modificarla, actualiza la fecha y añade una línea al "Historial de cambios" del
   final si el cambio es de fondo.
6. **Idioma:** todo en español. El español es idioma primario de Formelia por estrategia
   ("el español no es una traducción").

## Reglas de marca innegociables (resumen — detalle en `00-core/marca/`)

- Color primario: Forest Teal `#00786f` (familia teal 50–950). Éxito = teal, **no verde**.
- Tipografía: **Lexend** (títulos, branding) + **Geist** (cuerpo, UI).
- Las features de IA **no** usan violeta ni iconos "Sparkles" — grises neutros e iconos
  funcionales. El acento de acción siempre es teal.
- Tono: cercano, directo, **tuteo** (nunca voseo), imperativo, frases cortas, honesto
  ("Sin tarjeta", "Gratis para siempre"). Nombra el dolor antes de la solución.
- Headline canónico: **"Formularios que la gente sí termina."**

## Datos fijos del negocio (para no re-buscar)

- Planes: Free $0 · Pro $10/mes · Team $25/mes (hasta 5 miembros, $0 por puesto).
  500 créditos IA gratis/mes en todos los planes; Pro 2.000, Team 4.000. 1 crédito = 1.000 tokens.
- Beachhead: PYMEs de servicios hispanohablantes (1–50 empleados) que hoy usan
  Google Forms + WhatsApp + Sheets. Países: MX, CO, CL, AR, PE + España + hispanos en EE.UU.
- Personas: **Carolina** (coordinadora/dueña operativa, primaria), **el consultor multiplicador**
  (secundaria), el respondedor móvil/WhatsApp-first (terciaria).
- Métrica norte: **FAS** — Formularios Activos por Semana (publicados con ≥5 respuestas/semana).
- Lanzamiento público objetivo: **15-ago-2026**. Riesgo #1 declarado: **distribución**.
- Anti-pitch: nunca decir "Typeform con IA", "vamos por todo el mercado global", ni vender TAMs
  sin camino. Anti-posicionamiento: no somos research, no somos chatbot, no somos no-code amplio.
