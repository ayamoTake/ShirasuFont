#!/usr/bin/python3 
import fontforge
import os

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

    codepoint = ord(char)
    svg_path = os.path.join(SVG_DIR, filename)

    glyph = font.createChar(codepoint)
    glyph.clear()
    glyph.importOutlines(svg_path)

font_name = "Shirasu.ttf"
font.generate(font_name)
print(font_name, " created.")
