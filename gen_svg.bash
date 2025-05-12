#!/usr/bin/env bash

shopt -s nullglob nocaseglob
# file="$1"

img_dir="./glaph_images"
format="JPG"

for file in $img_dir/*.$format; do
    ./tosvg.bash $file
    echo "${file%.*}.svg" converted
done

gen_marked_cmd="gen_marked.py"
if [[ -f "$gen_marked_cmd" ]]; then
    python3 "$gen_marked_cmd"
fi

gen_small_cmd="gen_small.py"
if [[ -f "$gen_small_cmd" ]]; then
    python3 "$gen_small_cmd"
fi

