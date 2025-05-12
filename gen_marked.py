#!/usr/bin/python3 

from svgpathtools import svg2paths2, wsvg
import os


# 清音 + 濁点／半濁点 の合成リスト
combinations = [
    ("か", "dakuten", "が"),
    ("き", "dakuten", "ぎ"),
    ("く", "dakuten", "ぐ"),
    ("け", "dakuten", "げ"),
    ("こ", "dakuten", "ご"),
    ("は", "dakuten", "ば"),
    ("ひ", "dakuten", "び"),
    ("ふ", "dakuten", "ぶ"),
    ("へ", "dakuten", "べ"),
    ("ほ", "dakuten", "ぼ"),
    ("は", "handakuten", "ぱ"),
    ("ひ", "handakuten", "ぴ"),
    ("ふ", "handakuten", "ぷ"),
    ("へ", "handakuten", "ぺ"),
    ("ほ", "handakuten", "ぽ"),
]

img_file_dir="glaph_images"

from flip_paths import flip_paths_vertically
for base, mark, result in combinations:
    base_file = f"./{img_file_dir}/{base}.svg"
    mark_file = f"./{img_file_dir}/{mark}.svg"
    if not os.path.exists(base_file):
        print(f"Missing file: {base_file}")
        continue
    if not os.path.exists(mark_file):
        print(f"Missing file: {mark_file}")
        continue

    base_paths, base_atri, base_svg_attri = svg2paths2(base_file)
    mark_paths, mark_atri, mark_svg_attri = svg2paths2(mark_file)

    out_file = f"./{img_file_dir}/{result}.svg"
    base_paths = flip_paths_vertically(base_paths)
    mark_paths = flip_paths_vertically(mark_paths)
    wsvg(base_paths + mark_paths,
         attributes=base_atri + mark_atri,
         filename=out_file)
    print(f"{result}.svg saved.")

