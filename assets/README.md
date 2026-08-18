# Assets exportados

Aquí viven los archivos pesados que produce el trabajo de las áreas: vídeos, imágenes
renderizadas, exports de piezas. **Nada de esta carpeta se sube a GitHub** salvo este
README — está en el [`.gitignore`](../.gitignore) de la raíz.

## Por qué existe

Los binarios grandes no pertenecen al historial de git: lo engordan para siempre y no se
pueden diferenciar. Lo que sí se versiona es **cómo se generan** — la plantilla, la
especificación y la herramienta. El archivo final es un derivado y se puede volver a sacar
en cualquier momento desde su fuente.

Si necesitas compartir un exportable con alguien, súbelo a Drive; no lo metas en el repo.

## Convención

Un subdirectorio por pieza o campaña, con el mismo slug que su fuente:

```
assets/
  motion-identidad/     ← fuente en 01-diseno/assets/plantillas/motion-identidad/
```

Nombrado de archivo: `formelia-<pieza>-<variante>-<ancho>x<alto>.<ext>`.

## Inventario

| Carpeta | Qué contiene | Cómo se regenera |
| --- | --- | --- |
| `motion-identidad/` | Motion de marca. Cuatro MP4 para publicar (crema y teal, en 3:4 y 9:16) y cuatro con fondo transparente para componer (tinta oscura y clara, en `.mov` ProRes 4444 y `.webp` animado) | [`exportar.sh`](../01-diseno/assets/plantillas/motion-identidad/exportar.sh) y, para los transparentes, [la spec](../01-diseno/assets/plantillas/motion-identidad/motion-identidad.md#transparencia) |
| `2026-08/reel-imposible-desde-el-telefono-escenas/` | Las cuatro escenas animadas del reel del 16-ago en MP4 1080×1920 a 30 fps: formulario genérico (aparición y scroll; resaltados rojos), hoja de respuestas con filas vacías, y demo real de Formelia (prompt, tres slides, gracias) | Fuente al lado (`escenas.html` + `estilos.css`); `empaquetar.py` y luego `exportar-video.py --params "escena=N" --tamano 1080x1920` por cada escena |
| `2026-08/reel-pregunta-cara-escenas/` | Las tres escenas animadas del reel «La pregunta cara» en MP4 1080×1920 a 30 fps: texto libre vs selector (teclado iPhone, selección teal, gracias; 10 s), gráfico de abandono por pregunta sobre la pintura con la fila de la caída enmarcada en rojo (4 s), y el dock de IA cambiando el campo a selector con RadialSpinner (7 s) | Fuente al lado (`escenas.html` + `estilos.css`, pintura incrustada); `empaquetar.py` y luego `exportar-video.py --params "escena=N" --tamano 1080x1920` por cada escena |

Los `.mov` con alfa rondan los 55 MB cada uno: otra razón para que esta carpeta no entre
en git.
