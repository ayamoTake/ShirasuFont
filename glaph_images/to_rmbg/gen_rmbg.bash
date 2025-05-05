#!/usr/bin/env bash

shopt -s nullglob nocaseglob
format="JPG"
img_dir="."
for file in $img_dir/*.$format; do
    python3 ./remove_bg.py $file ../$file && echo remove "$file" bg. || echo failed removing bg of "$file".
done

