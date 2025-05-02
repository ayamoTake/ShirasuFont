#!/usr/bin/env bash

shopt -s nullglob nocaseglob
# file="$1"

for file in *.png; do
    base="${file%.png}"
    convert "${file}" -resize 1024x1024\! -monochrome -negate "$base.pbm" 
    potrace "$base.pbm" -s -o "$base.svg"  
    rm "$base.pbm"
    echo ${base}.svg converted
done

gen_marked_cmd="gen_marked.py"
if [[ -f "$gen_marked_cmd" ]]; then
    python3 "$gen_marked_cmd"
fi

gen_small_cmd="gen_small.py"
if [[ -f "$gen_small_cmd" ]]; then
    python3 "$gen_small_cmd"
fi

