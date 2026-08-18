# Memoria viva del CEO

> Este es el primer archivo que se lee al retomar el trabajo. Se actualiza al cierre de cada
> sesión significativa: estado, foco y movimientos recientes, siempre con fecha.

## Estado actual (2026-08-04)

- **Fase:** pre-lanzamiento. Lanzamiento público **FIJO 15-ago-2026** (en 11 días) — decisión
  del founder: se lanza con lo que haya.
- **Producto en soft launch:** cualquiera puede registrarse; sin anuncio. Audiencia: cero.
- **Estrategia H2 definida** (decisión
  [2026-08-04](decisiones/2026-08-04-estrategia-h2-2026.md)): 70% distribución / 30%
  producto · 4 avatares con corte a 2 el 30-sep · foco México+Colombia · IG/TikTok/LinkedIn/X
  (personal + marca) · blog propio en formelia.io · Claude produce, founder aprueba todo.
- **Riesgo #1:** distribución — 0 usuarios, 0 canal probado.
- **Bloqueantes del gate de julio SIN AUDITAR** (estado desconocido al 04-ago; el founder
  no lo tiene presente — detalle en [`operaciones/legal/`](operaciones/legal/README.md)):
  cierre legal (límite era 31-jul), economía de tokens, matriz `LimitDialog`, disclosure AI
  Act (vigente desde 02-ago). **Auditoría con evidencia: 05-ago.**

## Foco del mes (agosto 2026)

1. **05-ago: auditar bloqueantes** legales/económicos con evidencia (única tarea que puede
   forzar mitigaciones pre-lanzamiento; la fecha no se mueve).
2. Pre-lanzamiento (04–14): UTM/atribución, `llms.txt`, 12 plantillas-landing, comunidades
   MX/CO en modo aporte, teaser en redes (calendario sembrado).
3. **Lanzar el 15-ago** en todas las superficies + comunidades.
4. Post (16–31): `/blog` + 4 artículos, semanas temáticas por avatar, outreach consultoras,
   fricción de onboarding con feedback real.

## Decisiones recientes

- [2026-08-14 — El headline público abre con la promesa, no con el mecanismo](decisiones/2026-08-14-headline-promesa.md)
- [2026-08-04 — Estrategia operativa H2-2026 (avatares, canales, blog, recursos)](decisiones/2026-08-04-estrategia-h2-2026.md)
- [2026-08-04 — Reestructuración de áreas y reinicio de marketing](decisiones/2026-08-04-reestructuracion-areas.md)
- [2026-07-30 — Creación del entorno de gestión (este repo)](decisiones/2026-07-30-creacion-entorno-gestion.md)

## Últimos movimientos

- **2026-08-17** — **Escenas animadas del reel «La pregunta cara» exportadas**
  (`assets/2026-08/reel-pregunta-cara-escenas/`): tres MP4 1080×1920 a 30 fps para los
  bloques 22-29 y 34-42 del [brief](../02-marketing/redes/instagram/2026-08-16-reel-pregunta-cara/brief.md),
  aprobados por el founder tras cinco rondas de iteración en chat. Escena 1 (10 s): la misma
  pregunta como texto libre (teclado iPhone en gris, cursor) y como selector (radio cards,
  selección teal, pantalla de gracias); escena 2 (4 s): el gráfico real de abandono por
  pregunta sobre la pintura de la home, con la fila de la caída enmarcada en rojo sutil;
  escena 3 (7 s): el dock de IA cambiando el campo a selector, con el RadialSpinner real.
  Fidelidad copiada del código del producto (`DropoffWaterfall`, `OptionChip`, `AIActionDock`,
  literales de `messages/es`). Fuente junto a los MP4; pipeline `empaquetar.py` +
  `exportar-video.py`. El montaje con voz va en Final Cut; artes crudos a Drive.
- **2026-08-16** — **Skill nuevo `pantallas-reel`** (`.claude/skills/pantallas-reel/`):
  produce las pantallas animadas de un reel con UI real — captura la app con la cuenta demo
  siguiendo un plan JSON versionable (herramienta nueva
  [`capturar-ui.py`](../01-diseno/herramientas/capturar-ui.py), CDP sin dependencias),
  anima cada escena a 1080x1920 y exporta **un clip MP4 por escena** con las herramientas
  existentes (`?escena=N` sobre una sola pieza HTML): los planos a cámara salen como clips
  negros con su duración exacta y el montaje se hace en Final Cut sustituyéndolos por el
  rodaje. Credenciales de la cuenta demo en `.env` de la raíz, fuera de git. Probado de punta
  a punta con login simulado y export real por escena; falta el piloto contra la app
  corriendo (`formelia-app` en el puerto 3020).

- **2026-08-16** — **Dos guiones de reel aprobados y con brief de producción** para
  `@joinformelia` (pilar educación operativa, réplica en TikTok):
  [imposible desde el teléfono](../02-marketing/redes/instagram/2026-08-16-reel-imposible-desde-el-telefono/brief.md)
  (43 s, el orden de los campos espanta a quien responde) y
  [la pregunta cara](../02-marketing/redes/instagram/2026-08-16-reel-pregunta-cara/brief.md)
  (45 s, la pregunta de texto libre que cuesta respuestas). Cada brief lleva guion literal,
  tabla de producción escena a escena, ganchos alternativos y auditoría. Ajuste de honestidad
  hecho en sesión: la moraleja de "la pregunta cara" no promete señalado automático — muestra
  el modal de conversión por pregunta y el cambio de campo pidiéndoselo a la IA, que es lo que
  el producto hace hoy.

- **2026-08-14** — **La landing, commiteada y reescrita para convertir** (rama
  `feat/marketing-home-conversion` en `formelia-app`, siete commits, sin pushear). El rediseño
  que llevaba semanas sin commitear ya está en git, y encima se le aplicó una auditoría de
  conversión completa. Lo que cambia de fondo: **el headline invierte el orden**
  ([decisión](decisiones/2026-08-14-headline-promesa.md)); se añaden **reductores de riesgo**
  bajo los CTAs ("sin tarjeta · gratis para siempre · tus datos no entrenan modelos"), una
  **sección de dolor**, una **banda de prueba** con tres cifras verificables del producto
  (11 eventos por sesión, 13 análisis, 0 de contenido usado para entrenar), un bloque de
  **objeciones** y una **comparativa de flujo de trabajo** frente a "un formulario y una hoja de
  cálculo". El análisis sube del 85% al 51% de scroll.
  **Dos correcciones de honestidad que conviene conocer:** el copy prometía una IA a la que
  preguntarle lo que quisieras — no existe, son 13 análisis de catálogo — y dos maquetas
  dibujaban esa conversación; y la personalización se vendía como "paleta completa" cuando son
  18 acentos y 12 tipografías sin campo hexadecimal. Ambas corregidas en producto y en
  `marca/voz-y-tono.md`.
  **Pendiente antes del 15-ago:** revisar bios de redes y el teaser sembrado, que siguen el
  orden viejo del headline. Y quedan dos tareas abiertas en la landing: publicar un formulario
  real de demo (la constante `DEMO_FORM_SLUG` ya está lista para apuntarle) y convertir el hero
  en un campo de prompt real que arrastre el texto al alta.

- **2026-08-12** — **Motion de identidad**
  ([spec](../01-diseno/assets/plantillas/motion-identidad/motion-identidad.md)): pieza de
  apertura de las cuentas de redes. El isotipo se construye desde un rombo curvo que se
  divide en dos, cuenta qué hace Formelia y se abre al logotipo. 16,5 s en bucle, CSS puro
  sin JavaScript, en crema y teal, exportado a 3:4 (feed) y 9:16 (Reels y TikTok).
  Hallazgo aprovechable: **el isotipo son dos capas idénticas** desplazadas en diagonal que
  se tocan en una sola esquina, así que la animación sale de su propia geometría.
  Con la pieza quedan dos **herramientas reutilizables**
  ([`01-diseno/herramientas/`](../01-diseno/herramientas/README.md)): empaquetado a HTML
  autocontenido y grabación a MP4 por CDP, sin instalar dependencias. Se estrena también
  [`assets/`](../assets/README.md) en la raíz para exportables pesados, fuera de git.
  **Pendiente:** decidir si el 3:4 aguanta en el feed de Instagram o hace falta 4:5, y
  ponerle música al publicar (los MP4 salen mudos).

- **2026-08-11** — **Línea editorial de carruseles**
  ([spec](../01-diseno/assets/plantillas/carrusel/carrusel-editorial.md)): segundo repertorio de
  láminas alineado con el rediseño de la landing (arte pictórico de fondo, numerales
  contorneados, placas de crema, banda de cierre con grano). Patrones extraídos del código de
  `formelia-app/src/components/marketing/`, no de capturas. **Convive con la línea actual sin
  modificarla:** todo cuelga de la clase `linea-editorial`. Pendiente de decidir qué carruseles
  van en cada línea; por defecto sigue la actual. Riesgo: el rediseño de la landing sigue sin
  commitear, así que la línea puede desalinearse si cambia.
- **2026-08-10** — **Sistema de carruseles** en
  [`01-diseno/assets/plantillas/carrusel/`](../01-diseno/assets/plantillas/carrusel/carrusel.md):
  lienzo 1080x1350, rejilla de 6 columnas, zonas seguras, dos esquemas de color (claro para
  contenido, oscuro para portada y cierre), escala tipográfica propia y seis tipos de lámina,
  con la Pieza 4C montada de ejemplo. Diseñado para subirse como proyecto de sistema de diseño
  en Claude Design: el repo manda, Claude Design ejecuta. Discrepancia detectada y pendiente:
  teal-500 figura como `#159999` en [`marca/identidad-visual.md`](marca/identidad-visual.md) y
  como `#129f9f` en la fuente canónica del producto.
- **2026-08-08** — **Avatares: amplio primero, acotar con datos**
  ([decisión](decisiones/2026-08-08-avatares-amplio-primero.md)). Con audiencia cero, acotar
  antes de tener señal es adivinar: el contenido arranca lo más amplio posible y los cuatro
  escenarios pasan de ser el filtro de audiencia a ser la fuente del ejemplo concreto. Carolina
  se desliga de educación privada y de la vuelta a clases, y vuelve a ser la coordinadora u
  operativa de un negocio de servicios. El corte del 30-sep deja de ser automático de 4 a 2 y
  pasa a ser el primer acotamiento con datos. La segmentación por sector se mueve a plantillas,
  artículos y contacto directo (donde la persona ya declaró a qué se dedica). Reescrito
  [`avatares.md`](../02-marketing/avatares.md); actualizados
  [`posicionamiento.md`](posicionamiento.md) y la
  [estrategia de marketing](../02-marketing/estrategia.md).
- **2026-08-08** — **Regla de marca nueva: prohibido usar iconos y emoji** en todo lo que
  produzcamos (documentos, copy, posts, briefs, tablas, títulos). Los estados y etiquetas van
  con palabras. Única excepción: que el founder lo pida para una pieza concreta. Registrada
  en [`CLAUDE.md`](../CLAUDE.md), en [voz-y-tono.md](marca/voz-y-tono.md) (regla 10) y en el
  skill de marketing. Barrido completo del repo el mismo día: leyendas de estado del
  calendario, flujo de aprobación de marketing, roadmap, checklist legal y PRDs quedaron en
  palabras. La iconografía funcional de la UI del producto no cambia (la rige
  [identidad-visual.md](marca/identidad-visual.md)).
 **2026-08-06** — Nuevo headline canónico: **"Describe tu formulario y la IA lo crea"** (el
  mensaje funcional abre en frío; "Formularios que la gente sí termina" pasa a línea de apoyo
  — [decisión](decisiones/2026-08-06-headline-funcional.md)). Pendiente: adaptar el copy de
  la landing en `formelia-app` y revisar las piezas sembradas del calendario con el gancho
  nuevo.
**2026-07-30** — Se crea Formelia HQ (`cowork/`): estructura de áreas, estrategias iniciales
  por equipo y skills.

## Aprendizajes acumulados

*(Añadir aquí, con fecha, lo que el mercado nos vaya enseñando: qué canal funciona, qué mensaje
convierte, qué segmento paga. Nada de opiniones sin dato.)*

## Preguntas abiertas

- **¿En qué estado real quedaron los bloqueantes del gate de julio?** (auditoría 05-ago —
  entidad legal, DPAs, economía de tokens, LimitDialog, AI Act)
- ¿Qué 5 comunidades MX/CO concentran mejor a los 4 avatares? (definir esta semana para
  empezar a aportar antes del 15-ago)
- ¿El pricing en USD frena la conversión en MX/CO? (display en moneda local ya agendado
  para sep en el roadmap)
- ¿Aguanta el founder la cadencia de 2 grabaciones/sem + 6 superficies? (revisar con datos
  reales el 01-sep; si no, recortar superficies antes que calidad)
