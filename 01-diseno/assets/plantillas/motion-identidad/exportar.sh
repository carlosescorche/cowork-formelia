#!/usr/bin/env bash
# Formelia — Motion de identidad: los cuatro MP4 listos para publicar.
#
#   ./exportar.sh          # 30 fps
#   ./exportar.sh 60       # 60 fps
#
# Los vídeos van a assets/, que está en .gitignore: no se suben a GitHub.

set -euo pipefail
cd "$(dirname "$0")"

FPS="${1:-30}"
HERRAMIENTA="../../../herramientas/exportar-video.py"
PIEZA="motion-identidad-completo.html"
SALIDA="../../../../assets/motion-identidad"

# El HTML autocontenido no se versiona; se regenera si falta.
[ -f "$PIEZA" ] || python3 ../../../herramientas/empaquetar.py motion-identidad.html

for variante in crema teal; do
  python3 "$HERRAMIENTA" "$PIEZA" --fps "$FPS" \
    --tamano 1080x1440 --params "solo=${variante}" \
    --salida "${SALIDA}/formelia-motion-${variante}-1080x1440.mp4"

  python3 "$HERRAMIENTA" "$PIEZA" --fps "$FPS" \
    --tamano 1080x1920 --params "solo=${variante}&formato=9x16" \
    --salida "${SALIDA}/formelia-motion-${variante}-1080x1920.mp4"
done

echo
echo "Listos en ${SALIDA}"
