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

Los `.mov` con alfa rondan los 55 MB cada uno: otra razón para que esta carpeta no entre
en git.
