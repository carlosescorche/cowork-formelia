# Estrategia de marketing

> Documento vivo del equipo de Marketing. Última actualización: 2026-07-30
> Se subordina a [`00-core/posicionamiento.md`](../00-core/posicionamiento.md) y trabaja en
> pareja con [`04-growth/estrategia.md`](../04-growth/estrategia.md) (growth posee los canales y
> métricas de adquisición; marketing posee el mensaje y el contenido).

## Objetivo del área

Convertir el posicionamiento en **demanda medible**: que Carolina y el consultor multiplicador
descubran Formelia, entiendan en 5 segundos qué resuelve y lleguen a la landing a crear su primer
formulario. Métricas que posee marketing: alcance cualificado, CTR a landing, **signups por
fuente de contenido** (instrumentados por UTM).

Contribución a la métrica norte (FAS): cada pieza debe empujar a una de estas dos acciones —
crear un formulario o publicar/compartir uno.

## Los tres pilares de contenido

Todo el contenido cae en uno de estos tres pilares. Proporción objetivo: **50 / 30 / 20**.

1. **Educación operativa (50%)** — resolver el job-to-be-done, no hablar del producto.
   "Cómo hacer que la gente sí responda tu encuesta", "La ficha de inscripción que no espanta a
   los padres", "3 preguntas que matan tu NPS". El producto aparece como demostración, no como
   protagonista. Es el contenido que posiciona y el que los LLMs citan.
2. **Producto en acción (30%)** — demos de ≤60 segundos: del prompt al formulario publicado,
   compartir por WhatsApp con QR, la IA resumiendo 200 respuestas. Siempre producto real, nunca
   mockups. El "wow" honesto: velocidad y español.
3. **Build in public (20%)** — la historia del founder: métricas reales, decisiones, errores.
   Genera confianza (una PYME entrega sus datos a una marca con cara) y atrae al consultor
   multiplicador y a la comunidad maker hispana.

## Estrategia por red social

Detalle operativo en el README de cada carpeta. Resumen:

| Red | Rol estratégico | Audiencia | Frecuencia | Formatos |
| --- | --- | --- | --- | --- |
| [Instagram](redes/instagram/README.md) | Canal principal para Carolina: educación visual + demos | Dueñas/coordinadoras de PYMEs | 4 posts/sem + 3 stories/sem | Carruseles, Reels, stories |
| [TikTok](redes/tiktok/README.md) | Alcance y demos rápidas; probar hooks | PYMEs jóvenes, emprendedores LATAM | 3–4 videos/sem | Video vertical ≤45s |
| [LinkedIn](redes/linkedin/README.md) | Consultores, agencias y build in public | Consultor multiplicador, agencias | 3 posts/sem | Texto + carrusel documento |
| [X (Twitter)](redes/x-twitter/README.md) | Build in public + comunidad maker hispana | Makers, early adopters, inversores | 4–5 tuits/sem | Hilos, capturas, métricas |
| [YouTube](redes/youtube/README.md) | SEO de video: tutoriales por JTBD | Búsqueda con intención | 1 video/sem (desde sep) | Tutorial 3–8 min + Shorts |

**Regla de foco:** hasta el 30-sep-2026, Instagram y TikTok son prioridad 1 (donde vive
Carolina); LinkedIn y X prioridad 2 (se alimentan de recortes); YouTube arranca en septiembre.
Revisión mensual: la red que no muestre tracción tras 8 semanas de ejecución consistente se
reduce a repost.

## Qué transmite cada red (posicionamiento por canal)

- **Instagram/TikTok:** "esto me ahorra horas y se ve profesional" — beneficio, velocidad,
  estética. Cero jerga.
- **LinkedIn:** "esto me hace ganar dinero con mis clientes" — casos, plantillas por industria,
  programa de partners cuando exista.
- **X:** "este founder va en serio y el producto es sólido" — números reales, decisiones
  técnicas, honestidad.
- **YouTube:** "así se hace exactamente" — tutoriales que responden búsquedas operativas
  ("cómo hacer un formulario de inscripción").

## Lenguaje y diseño (resumen — manda [`01-marca/`](../01-marca/estrategia.md))

- Voz: tuteo, imperativo, dolor antes que solución, sin hype de IA. Ver
  [voz-y-tono.md](../01-marca/voz-y-tono.md).
- Visual: teal + crema, Lexend/Geist, un acento por pieza, screenshots reales, captions siempre
  en video. Ver [identidad-visual.md](../01-marca/identidad-visual.md).
- CTA estándar: **"Crear formulario gratis"** → landing con UTM
  (`utm_source=<red>&utm_medium=social&utm_campaign=<campaña>`).

## SEO y blog (compounding — coordina con growth)

El SEO es de **intención operativa, no de categoría**: no "form builder" sino "formulario de
inscripción para curso", "ficha de ingreso de pacientes", "formulario de brief para clientes",
por país. Cada plantilla pública del producto es una landing indexable. El blog
([blog-seo/](blog-seo/README.md)) publica 2 artículos/sem desde agosto: 1 por JTBD + 1 de
comparativa/educación. Todo artículo enlaza a una plantilla clonable.

**AI-search primero:** el contenido se estructura para ser citado por LLMs (respuestas directas,
listas, datos con fuente, `llms.txt` en el sitio). En español la competencia por ser "la
respuesta del LLM" es casi nula — es nuestra asimetría de timing.

## Calendario y cadencia de trabajo

- Planificación semanal en [calendario-editorial.md](calendario-editorial.md) (viernes se deja
  lista la semana siguiente).
- Las piezas se producen y almacenan en `redes/<red>/` con la convención de nombrado de cada
  README; el arte final se genera a partir de esos briefs.
- Revisión mensual (día 1): métricas por red y por pilar → matar o doblar formatos.

## Campaña activa

**Lanzamiento 15-ago-2026** — brief en [campanas/](campanas/README.md). Fases: teaser (4–14
ago), lanzamiento (15–22 ago), consolidación (hasta 30 sep).

## Historial de cambios

- 2026-07-30 — Versión inicial.
