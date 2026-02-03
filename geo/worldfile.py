import os

def make_worldfile(png_path, tile_info, zoom):
    """
    根据 tile 信息生成 .pgw
    tile_info = (min_x, min_y, tile_w, tile_h)
    """

    min_x, min_y, tw, th = tile_info

    # 分辨率（米/像素）： WebMercator
    initial_res = 156543.03392804097
    res = initial_res / (2 ** zoom)

    # 世界文件六行
    A =  res        # 像素宽度（米/像素）
    D =  0
    B =  0
    E = -res        # 像素高度（米/像素）
    C = min_x * tw * res
    F = -min_y * th * res

    wld_path = png_path.replace(".png", ".pgw")

    with open(wld_path, "w") as f:
        f.write(f"{A}\n{D}\n{B}\n{E}\n{C}\n{F}\n")

    print(f"[OK] 世界文件生成：{wld_path}")
    return wld_path