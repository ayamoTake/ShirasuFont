#!/usr/bin/env bash

file="$1"
format="${file##*.}"
pbmfile="${file%.$format}.pbm"
svgfile="${file%.$format}.svg"

convert "$file" -resize 1024x1024\! -monochrome -negate "$pbmfile"
potrace "$pbmfile" -s -t 100 --opttolerance 0.4 -o "$svgfile" 

rm "$pbmfile"
