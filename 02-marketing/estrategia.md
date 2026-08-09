# Estrategia de marketing

> Documento vivo del equipo de Marketing. Última actualización: 2026-08-04 (v2)
> Definida en sesión de estrategia con el founder — decisión:
> [estrategia H2-2026](../00-core/decisiones/2026-08-04-estrategia-h2-2026.md).
> Se subordina a [`00-core/posicionamiento.md`](../00-core/posicionamiento.md); los canales y
> su medición son de [growth](../03-growth/estrategia.md); marketing posee mensaje y contenido.

## Restricción de diseño (todo lo demás se deriva de esto)

**Una persona, ~10h/semana para distribución, audiencia cero, aprobación del founder para
todo.** La estrategia solo vale si es ejecutable en ese presupuesto: contenido en batch,
reutilización agresiva entre redes, y Claude produce todos los borradores.

## Objetivo del área

Que los 4 [avatares](avatares.md) descubran Formelia, entiendan en 5 segundos qué resuelve y
lleguen a crear su primer formulario. Métricas que posee marketing: alcance cualificado, CTR
a landing, signups por fuente de contenido (UTM por pieza). Cada pieza empuja una de dos
acciones: **crear un formulario o compartir uno.**

## Pilares de contenido (proporción 50/30/20)

1. **Educación operativa (50%)** — resolver el job-to-be-done del avatar de la semana, no
   hablar del producto. "La ficha de inscripción que los padres sí terminan", "El brief que
   tus clientes sí completan". El producto aparece como demostración.
2. **Producto en acción (30%)** — demos ≤60s: del prompt al formulario publicado, compartir
   por WhatsApp con QR, la IA resumiendo 200 respuestas. Siempre producto real.
3. **Build in public (20%)** — la historia del founder en primera persona: métricas reales,
   decisiones, errores. Vive en las cuentas personales.

## Superficies y cadencia (4 canales, 6 superficies)

| Superficie | Rol | Cadencia | Formato |
| --- | --- | --- | --- |
| **IG @joinformelia** | Canal principal de avatares (Camila, Carolina) | 3 reels + 1 carrusel/sem + 3 stories | Reels ≤45s, carrusel educativo |
| **TikTok @joinformelia** | Alcance frío; mismos videos que IG | 3 videos/sem (reutilizados) | Video vertical |
| **LinkedIn personal** | Build in public + avatar Valeria | 3 posts/sem | Texto + clip o carrusel-documento |
| **LinkedIn @joinformelia** | Presencia de marca; reutiliza | 2 posts/sem (repurpose) | Carrusel + clip |
| **X personal** | Build in public + avatar Diego | 4 tuits/sem | Recortes de LinkedIn, números, capturas |
| **IG personal** | BTS y cercanía; amplifica la marca | 3 stories/sem + repost | Stories crudas |

**Regla de producción:** todo el video de la semana sale de **2 sesiones de grabación de
45 min** (founder a cámara + screencast). Una pieza madre → 4–6 derivados. Nada se produce
para una sola red.

**Frontera con la marca personal:** este documento define qué aportan las superficies
personales a la distribución de Formelia (cadencia, pilares, CTAs). La identidad personal
del founder (narrativa, pilares propios, voz, red) se gestiona en su repo aparte
(`../cowork-personal/`); las piezas personales se producen igualmente en el lote semanal
compartido, etiquetadas `cuenta: personal`.

## Semana tipo (el sistema tú + Claude)

| Día | Founder (~2h/día distribución) | Claude entrega |
| --- | --- | --- |
| Lun | Aprobar lote semanal (45m) + comunidades (30m) | Lote completo: guiones, copys, specs de piezas, artículo 1 |
| Mar | Grabar batch A (45m) + comunidades (30m) | Cortes/captions listos para revisar |
| Mié | Aprobar cortes; Claude programa lo aprobado vía MCP (45m) | Semana programada en Metricool + calendario actualizado |
| Jue | Grabar batch B (45m) + outreach LinkedIn (30m) | Artículo 2 + mensajes de outreach personalizados |
| Vie | Aprobar blog + revisión semanal de métricas (45m) | Informe semanal: qué funcionó, qué ajustar |

## Blog — en formelia.io (decidido, no Substack)

- **Dónde:** `/blog` dentro de la app Next.js (MDX). El SEO y la citabilidad AI-search se
  acumulan en dominio propio — la asimetría del negocio. (Construcción: 16–31 ago, ver
  [roadmap](../04-producto/roadmap.md).)
- **Cadencia:** 2 artículos/sem — 1 JTBD del avatar en rotación + 1 comparativa/educación
  ("Typeform vs Formelia en pesos", "5 plantillas de ficha de ingreso").
- **Estructura AI-search en todo artículo:** respuesta directa en el primer párrafo → paso a
  paso → plantilla clonable → FAQ → datos con fuente. Keywords de intención operativa por
  país (MX/CO primero), definidas con growth.
- **Newsletter:** quincenal desde septiembre con Resend ("lo nuevo + 1 truco + 1 plantilla").

## Herramientas (~$100/mes)

| Herramienta | Para qué | Costo |
| --- | --- | --- |
| Metricool | Programar IG/TikTok/LinkedIn/X + métricas unificadas + inbox | ~$54 |
| Notion (Free) | **Tablero de aprobación**: calendario visual, estados y comentarios por pieza (vía MCP oficial) | $0 |
| Higgsfield (MCP oficial) | Imágenes 4K editoriales y video cinemático ≤15s (Kling/Veo/Sora/Seedance/Soul) — el motor visual del feed | ~$49 (créditos) |
| HeyGen (MCP oficial) | Videos de avatar para contenido explicativo/educativo (nunca "hace de" founder) | ~$29 |
| CapCut Pro | Edición de video vertical (reels/TikTok) con captions de marca | ~$10 |
| Screen Studio | Demos de producto en pantalla con calidad alta — la UI siempre es real | ~$89 única |
| Canva Pro | Ajustes manuales puntuales con Brand Kit | ~$15 |
| Resend | Newsletter quincenal (desde sep) | ~$20 |

**Producción de arte (v2 — dirección de arte por pieza, no plantillas fijas):**

1. **Generativa AI (vía MCP, la capa principal del feed):** cada pieza lleva su *dirección de
   arte* propia — concepto, referencia de tendencia actual, prompt y modelo — escrita por
   Claude en la tarjeta de Notion. Claude genera **2–3 variantes** con Higgsfield (estáticos
   editoriales, hooks cinemáticos, b-roll realista, personajes consistentes por avatar) y las
   sube a Drive; el founder elige o pide otra ronda en la revisión 2. HeyGen cubre videos
   explicativos con avatar. La coherencia de marca no viene de un layout repetido sino del
   **sistema visual**: paleta teal/crema, tipografía (Lexend/Geist) cuando hay texto, y tono
   fotográfico consistente.
2. **Real (irremplazable):** el founder a cámara para build in public e historias — un avatar
   jamás lo suple; y la UI del producto siempre grabada de verdad (Screen Studio). El video
   generado puede rodear la demo (intro, contexto, hook), nunca sustituirla.
3. **Funcional:** plantillas-código solo para assets seriados no-creativos (OG images de blog
   y plantillas); Canva para ajustes puntuales.

**Reglas duras de la capa AI:** UI inventada prohibida · el avatar sintético nunca narra la
vida del founder ni simula ser él · etiquetas de contenido generado donde la plataforma o el
AI Act lo exijan · el hype de IA sigue prohibido en el *mensaje* (la IA es herramienta de
producción, no tema del contenido).

$0 en ads hasta PMF (regla de growth). El resto del presupuesto queda en reserva.

**Operación vía MCP (Claude conectado a las herramientas):** Metricool tiene MCP oficial
(`https://ai.metricool.com/mcp`, OAuth — analytics, programación e informes; incluido con el
plan que ya presupuestamos) y PostHog también (`https://mcp-eu.posthog.com/mcp`, gratis).
Conectados ambos: Claude programa en Metricool las piezas aprobadas, y cruza métricas de
Metricool (redes) + PostHog (sitio/embudo) + Supabase (FAS/activación) para el informe
semanal del viernes y el mensual de matar/doblar. Regla intacta: **Claude solo programa lo
que el founder aprobó.**

**Flujo de aprobación (Notion como tablero, decidido 2026-08-04):** las piezas viven en una
base de Notion (vista calendario + kanban). Dos compuertas de aprobación por pieza:

```
💡 idea → ✍️ guion/copy → 👀 revisión 1 (apruebas el guion) → 🎨 producción
       → 🖼️ revisión 2 (apruebas el arte final) → ✅ aprobada → 🗓️ programada → 📊 publicada
```

Claude crea las piezas vía MCP con el copy o guion dentro; el founder revisa desde el móvil,
comenta cambios o avanza el estado; Claude aplica cambios, y solo lo aprobado pasa a
Metricool. El `calendario-editorial.md` del repo queda como archivo estratégico — la
operación diaria vive en Notion (una sola fuente operativa).

**Assets (imágenes y videos) — Google Drive como almacén maestro:** los binarios NO van al
repo (infla git) ni se suben a Notion (el plan free limita a 5MB/archivo y sus URLs firmadas
caducan — Metricool no podría leerlas). Estructura en Drive espejando la convención de
piezas: `Formelia Assets/AAAA-MM/<slug-pieza>/` con `raw/` (clips crudos) y `final/`
(exports de CapCut/Canva, nombrados `slug-superficie-v1.ext`). Cada tarjeta de Notion
embebe el enlace de Drive del arte final — el video se reproduce inline para validarlo — y
Claude programa en Metricool desde ese enlace estable. El repo guarda solo briefs y specs;
los assets de marca reutilizables (logos, plantillas) siguen en `01-diseno/assets/` por su
propia convención.

## Medición

- UTM en todo: `utm_source=<red>&utm_medium=social&utm_campaign=avatar-<slug>` (o campaña).
- Revisión semanal (viernes, con Claude): resultados a 7 días por pieza en el calendario.
- Revisión mensual (día 1): por red, pilar y avatar → matar o doblar formatos.
- **Corte de avatares 30-sep** según [avatares.md](avatares.md).

## Lenguaje y diseño (manda [`00-core/marca/`](../00-core/marca/))

Tuteo, imperativo, dolor antes que solución, sin hype de IA. Teal + crema, Lexend/Geist,
screenshots reales, captions siempre. Voz por cuenta (personal vs marca) definida en
[voz-y-tono.md](../00-core/marca/voz-y-tono.md). CTA estándar: **"Crear formulario gratis"**.
Anti-pitch: jamás "Typeform con IA"; jamás features del roadmap como existentes.

## Campaña activa

**Lanzamiento 15-ago-2026:** teaser (6–14 ago, build in public del founder + primeras demos)
→ lanzamiento (15–22 ago, pieza fuerte en todas las superficies + comunidades) →
consolidación (hasta 30-sep, semanas temáticas por avatar). Brief en [campanas/](campanas/README.md).

## Historial de cambios

- 2026-08-04 — **v2.** Reescrita tras el reinicio: 4 avatares con corte, 6 superficies en 4
  canales, blog propio en formelia.io, sistema de producción founder+Claude, herramientas.
- 2026-08-04 — Reinicio total (v1 descartada).
- 2026-07-30 — Versión inicial (descartada).
