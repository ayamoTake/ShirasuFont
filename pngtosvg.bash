#!/usr/bin/env bash

shopt -s nullglob nocaseglob
# file="$1"

img_dir="./glaph_images"

for pngfile in *.png; do
    base="${img_dir}/${pngfile%.png}"
    pbmfile="$base.pbm"
    svgfile="$base.svg"
    convert "${pngfile}" -resize 1024x1024\! -monochrome -negate "$pbmfile"
    potrace "$pbmfile" -s -o "$svgfile"  
    rm "$pbmfile"
    echo "$svgfile" converted
done

gen_marked_cmd="gen_marked.py"
if [[ -f "$gen_marked_cmd" ]]; then
    python3 "$gen_marked_cmd"
fi

gen_small_cmd="gen_small.py"
if [[ -f "$gen_small_cmd" ]]; then
    python3 "$gen_small_cmd"
fi

