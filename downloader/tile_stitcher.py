import os
from PIL import Image

def stitch_tiles(tile_folder, output_image):
    """
    将整个瓦片文件夹拼接成一张大图。

    文件名格式要求：
        {zoom}_{x}_{y}.png

    参数：
        tile_folder   : 下载瓦片的文件夹
        output_image  : 最终输出的大图路径 (PNG)
    """
    # 读取所有瓦片文件
    tiles = [f for f in os.listdir(tile_folder) if f.endswith(".png")]

    if not tiles:
        raise ValueError("瓦片文件夹为空，请先下载瓦片。")

    # 解析文件名，提取所有 x,y
    xs = []
    ys = []
    images = {}

    for filename in tiles:
        z, x, y = filename.replace(".png", "").split("_")
        x = int(x)
        y = int(y)

        xs.append(x)
        ys.append(y)

        img_path = os.path.join(tile_folder, filename)
        images[(x, y)] = Image.open(img_path)

    # 计算瓦片范围
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    tile_width, tile_height = images[(min_x, min_y)].size

    # 输出大图尺寸
    out_width = (max_x - min_x + 1) * tile_width
    out_height = (max_y - min_y + 1) * tile_height

    print(f"拼接大图大小：{out_width} x {out_height}")

    # 创建空白大图
    big_map = Image.new("RGB", (out_width, out_height))

    # 将所有瓦片贴上去
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in images:
                img = images[(x, y)]
                px = (x - min_x) * tile_width
                py = (y - min_y) * tile_height
                big_map.paste(img, (px, py))
            else:
                print(f"警告：瓦片缺失 x={x}, y={y}")

    # 保存大图
    os.makedirs(os.path.dirname(output_image), exist_ok=True)
    big_map.save(output_image)

    print(f"拼接完成 → {output_image}")

    return output_image
