#!/usr/bin/fontforge -script 

import fontforge
import os


def clone_char(ascii_name, dist_name, font):
    if dist_name in font:
        font.removeGlyph(dist_name)
    dist = font.createChar(-1, dist_name)
    dist.references = [(ascii_name, (1, 0, 0, 1, 0, 0,))]
    dist.width = 1024


def set_local_and_hwid(font, num):
    ascii_name = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][num]

    locl_name = f"{ascii_name}.locl"
    clone_char(ascii_name, locl_name, font)

    hwid_name = f"{ascii_name}.hwid"
    clone_char(ascii_name, hwid_name, font)


font = fontforge.open("original.ttf")
font.encoding = "UnicodeFull"
font.fontname = "ShirasuFont-Regular"
font.familyname = "ShirasuFont"
font.fullname = "Shirasu Font Regular"
font.weight = "Regular"
font.version = "1.0"
font.os2_weight = 400  # Regular


font.appendSFNTName(0x409, 'Family', 'ShirasuFont')
font.appendSFNTName(0x409, 'SubFamily', 'Regular')
font.appendSFNTName(0x409, 'Fullname', 'Shirasu Font Regular')

font.appendSFNTName(0x411, 'Family', 'しらすフォント')
font.appendSFNTName(0x411, 'SubFamily', 'レギュラー')
font.appendSFNTName(0x411, 'Fullname', 'しらすフォント レギュラー')


SVG_DIR = "glaph_images"

for filename in os.listdir(SVG_DIR):
    if not filename.endswith(".svg"):
        continue

    char = os.path.splitext(filename)[0]
    if len(char) != 1:
        continue

    print(f'{filename} loading...')
    codepoint = ord(char)
    svg_path = os.path.join(SVG_DIR, filename)

    glyph = font.createChar(codepoint)  # 既存があればそのまま取得
    glyph.clear(1)
    glyph.importOutlines(svg_path)     # SVGからアウトライン読み込み
    glyph.width = 1024

    if '0' <= char <= '9':
        # 全角数字の処理.
        glyph = font.createChar(0xFF10 + int(char))
        glyph.clear(1)
        glyph.importOutlines(svg_path)     # SVGからアウトライン読み込み
        glyph.width = 1024

        set_local_and_hwid(font, int(char))


font_name = "Shirasu.ttf"
font.generate(font_name, flags=("opentype"))
print(font_name, " created.")
