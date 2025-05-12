#!/usr/bin/python3 

from svgpathtools import svg2paths, wsvg
import os
from flip_paths import flip_paths_vertically

combinations = [
    ("あ", "ぁ"),
    ("い", "ぃ"),
    ("う", "ぅ"),
    ("え", "ぇ"),
    ("お", "ぉ"),
    ("つ", "っ"),
    ("や", "ゃ"),
    ("ゆ", "ゅ"),
    ("よ", "ょ"),
    ("わ", "ゎ"),
    ("か", "ゕ"),
    ("け", "ゖ"),
]

img_file_dir="glaph_images"

for base, small in combinations:
    base_file = f"./{img_file_dir}/{base}.svg"
    if not os.path.exists(base_file):
        print(f"Missing file: {base_file}")
        continue

    base_paths, base_atri = svg2paths(base_file)

    base_paths = flip_paths_vertically(base_paths)
    base_paths = [p.scaled(sx=0.6, sy=0.6) for p in base_paths]

    out_file = f"./{img_file_dir}/{small}.svg"
    wsvg(base_paths , attributes=base_atri , filename=out_file)
    print(f"{out_file} saved.")

