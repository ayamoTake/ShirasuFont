#!/usr/bin/python3

# https://qiita.com/kotai2003/items/2cddf1b3e17c728439b0

import cv2
from rembg import remove
from PIL import Image
import numpy as np
import io
import os
import sys


def remove_background(input_image_path):
    # 背景を削除（保存せず返す）
    try:
        input_image = Image.open(input_image_path)
    except IOError:
        print(f"Error: Cannot open {input_image_path}")
        return None

    output_image = remove(input_image)  # PIL.Image形式
    return output_image


def apply_mask_to_background(pil_image):
    # PILからNumPy配列（RGBA）へ変換
    rgba_image = np.array(pil_image)
    if rgba_image.shape[2] != 4:
        print("Error: Image does not have alpha channel.")
        return None

    alpha_channel = rgba_image[:, :, 3]

    # 黒背景を作成（RGBA形式）
    black_background = np.zeros_like(rgba_image, dtype=np.uint8)

    # 前景（人物など）だけを抽出
    for c in range(3):  # R, G, B チャンネル
        black_background[:, :, c] = rgba_image[:, :, c] * (alpha_channel / 255)

    # アルファを完全に不透明に
    black_background[:, :, 3] = 255

    return black_background


def remove_bg_save(input_path, output_path=None):
    if output_path is None:
        output_path = input_path

    # 背景除去（保存なし）
    removed_image = remove_background(input_path)
    if removed_image is None:
        return

    base_name = os.path.splitext(input_path)[0]

    # 黒背景合成
    result_image = apply_mask_to_background(removed_image)
    if result_image is not None:
        rgb_image = cv2.cvtColor(result_image, cv2.COLOR_RGBA2RGB)
        cv2.imwrite(output_path, rgb_image)  # ✅


def main():
    args = sys.argv
    if len(args) < 2:
        print(f'Usage: {args[0]} filename <outfile>')
        return

    filename = args[1]
    name, ext = os.path.splitext(filename)
    outfile = f'{name}_nobg{ext}'

    if len(args) >= 3:
        outfile = args[2]

    remove_bg_save(filename, outfile)

if __name__ == "__main__":
    main()
