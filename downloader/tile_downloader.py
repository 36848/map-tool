import os
import requests

def download_tile(x, y, z, save_path):
    """
    下载单个瓦片 (XYZ 格式)
    默认采用 OpenStreetMap 瓦片服务 (免费)
    """
    url = f"https://tile.openstreetmap.org/{z}/{x}/{y}.png"

    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        return True
    else:
        print(f"[WARN] 无法下载瓦片: {url}")
        return False


def download_tiles(tile_range, output_folder):
    """
    批量下载整个瓦片范围
    参数 tile_range = {min_x, max_x, min_y, max_y, zoom}
    """
    os.makedirs(output_folder, exist_ok=True)

    zoom = tile_range["zoom"]

    for x in range(tile_range["min_x"], tile_range["max_x"] + 1):
        for y in range(tile_range["min_y"], tile_range["max_y"] + 1):

            save_name = f"{zoom}_{x}_{y}.png"
            save_path = os.path.join(output_folder, save_name)

            print(f"Downloading: z={zoom}, x={x}, y={y}")

            download_tile(x, y, zoom, save_path)

    print("ok！")