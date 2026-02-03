import os
from PIL import Image

def stitch_tiles(tile_folder, output_image):
    """
    拼接瓦片为大地图
    """
    tiles = [f for f in os.listdir(tile_folder) if f.endswith(".png")]

    if not tiles:
        raise ValueError("瓦片为空")

    xs, ys = [], []
    images = {}

    for fn in tiles:
        z, x, y = fn.replace(".png", "").split("_")
        x = int(x)
        y = int(y)
        xs.append(x)
        ys.append(y)
        images[(x, y)] = Image.open(os.path.join(tile_folder, fn))

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    tw, th = images[(min_x, min_y)].size

    W = (max_x - min_x + 1) * tw
    H = (max_y - min_y + 1) * th

    print(f"拼接尺寸：{W} x {H}")

    big = Image.new("RGB", (W, H))

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in images:
                px = (x - min_x) * tw
                py = (y - min_y) * th
                big.paste(images[(x, y)], (px, py))

    os.makedirs(os.path.dirname(output_image), exist_ok=True)
    big.save(output_image)

    print(f"[OK] 拼接完成 → {output_image}")

    return output_image, (min_x, min_y, tw, th)
