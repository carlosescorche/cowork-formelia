# El headline público abre con la promesa, no con el mecanismo

- **Fecha:** 2026-08-14
- **Estado:** Vigente. Supersede la decisión del 2026-08-06 (headline funcional), cuyo archivo ya no está en este repo pero cuyo resultado seguía vigente en `posicionamiento.md` y `marca/voz-y-tono.md`.
- **Área(s) afectada(s):** core (marca), marketing

## Contexto

El 2026-08-06 se fijó **"Describe tu formulario y la IA lo crea"** como headline canónico y se
bajó **"Formularios que la gente sí termina"** a línea de apoyo. El razonamiento registrado en
`posicionamiento.md` fue que la promesa "ya no abre en frío: exige un contexto que una audiencia
de cero no tiene".

Ocho días después, dos cosas cambiaron.

La primera es la landing. El rediseño que se commiteó hoy en `formelia-app`
(rama `feat/marketing-home-conversion`) añadió tres bloques que antes no existían: una sección de
dolor que abre con "El formulario se envía. El problema empieza después.", una banda de prueba
con cifras del producto, y una comparativa titulada "La diferencia no está en el formulario. Está
en lo que pasa después.". El contexto que en agosto no existía ahora lo construye la propia página
en las dos primeras pantallas.

La segunda es que ese mismo trabajo dejó la página discutiendo consigo misma: un h1 que lidera con
crear formularios y un cuerpo que argumenta que crear formularios es precisamente donde no está la
diferencia.

A eso se suma que el mecanismo se comoditizó. Descríbelo-y-la-IA-lo-arma lo ofrecen hoy Typeform,
Tally, Fillout, Jotform y el propio Google Forms con Gemini. El headline describía la categoría,
no a Formelia.

Se decide a un día del lanzamiento del 15-ago, con audiencia cero. El coste de cambiarlo ahora es
mínimo por la misma razón que lo hace incómodo: no hay nadie que haya memorizado el anterior.

## Decisión

**"Formularios que la gente sí termina"** pasa a ser el headline público canónico: h1 de la
landing, meta title, tarjeta OG y primera línea de bio. **"Descríbelo con tus palabras y la IA lo
crea"** pasa a línea de apoyo y subtítulo.

El mecanismo no desaparece: explica cómo se cumple la promesa, que es el trabajo de un subtítulo.

## Alternativas consideradas

1. **Mantener el orden del 2026-08-06** — el argumento de agosto sigue siendo el mejor en contra:
   la promesa exige contexto y la prueba de que la gente termina no la tenemos todavía, porque
   estamos pre-lanzamiento. Se descarta porque la landing ahora aporta ese contexto ella misma y
   porque el titular alternativo caduca en cuanto un competidor iguala la feature, cosa que ya
   ocurrió.
2. **Buscar una tercera frase que combine promesa y mecanismo** — se probaron varias
   construcciones. Todas salen más largas y menos filosas que cualquiera de las dos frases que ya
   existen. Se descarta.
3. **Dejar el headline y cambiar el titular de la comparativa**, que es el que evidencia la
   contradicción. Se descarta: ese titular es correcto y renunciar a él para salvar el h1 es
   resolver el síntoma.

## Consecuencias

- `00-core/posicionamiento.md`: actualizado. Headline canónico y línea de apoyo intercambiados.
- `00-core/marca/voz-y-tono.md`: actualizado en "Frases canónicas". Cambia también
  **"El formulario se ve tuyo, no de la herramienta con la que lo hiciste"**, que se retira: con
  18 acentos predefinidos y 12 tipografías, sin campo hexadecimal, no podemos afirmar que el
  formulario se vea igual que la marca del cliente. La sustituye "Quien lo abre ve tu marca, no un
  formulario cualquiera", que habla de percepción y sí se sostiene.
- Todo lo publicado con el orden anterior queda desalineado: **bios de redes**
  (`00-core/marca/bios-redes.md`), teaser sembrado en el calendario y cualquier pieza de la línea
  editorial de carruseles que use el h1. Revisar antes del 15-ago.
- Riesgo aceptado: lideramos con una afirmación que no podemos probar con datos. La respalda el
  diseño del producto (una pregunta a la vez, progreso guardado, abandono por página), no una
  métrica de finalización propia. En cuanto haya volumen real, esa cifra es la primera que hay que
  medir y publicar.
- Riesgo aceptado: la animación del hero sigue enfatizando la construcción del formulario, así que
  ilustra la línea de apoyo y no el h1. Queda anotado en el componente.

## Criterio de revisión

Dos gatillos. El primero, tener tráfico suficiente para testear de verdad: del orden de 40.000
visitas o 400 conversiones al mes. Antes de eso cualquier test da conclusiones falsas y la
decisión se sostiene por criterio, no por dato. El segundo, la propia métrica de finalización: si
al acumular respuestas reales la tasa no es notablemente mejor que la de un formulario
convencional, el headline promete algo que el producto no cumple y hay que cambiarlo, no
defenderlo.
