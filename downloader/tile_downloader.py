import os
import time
import requests
from config import MAP_SOURCE, MAP_SOURCES, MAPTILER_KEY, USER_AGENT

def build_tile_url(x, y, z):
    """根据地图源生成正确的瓦片 URL"""

    url_template = MAP_SOURCES[MAP_SOURCE]

    # MapTiler 需要 KEY 替换
    url = url_template.format(
        z=z,
        x=x,
        y=y,
        MAPTILER_KEY=MAPTILER_KEY
    )

    return url


def download_tile(x, y, z, save_path):
    """
    下载单个瓦片，根据 MAP_SOURCE 自动选择地图源
    """

    url = build_tile_url(x, y, z)

    headers = {
        "User-Agent": USER_AGENT
    }

    try:
        resp = requests.get(url, headers=headers, timeout=10)
    except Exception as e:
        print(f"[ERROR] {url} -> {e}")
        return False

    if resp.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(resp.content)
        return True
    else:
        print(f"[WARN] HTTP {resp.status_code}: {url}")
        return False


def download_tiles(tile_range, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    z = tile_range["zoom"]

    for x in range(tile_range["min_x"], tile_range["max_x"] + 1):
        for y in range(tile_range["min_y"], tile_range["max_y"] + 1):

            save_name = f"{z}_{x}_{y}.png"
            save_path = os.path.join(output_folder, save_name)

            print(f"[{MAP_SOURCE}] Downloading z={z}, x={x}, y={y}")

            ok = download_tile(x, y, z, save_path)

            if not ok:
                print(f"[WARN] 瓦片失败 z={z}, x={x}, y={y}")

            time.sleep(0.15)

    print("[OK] 批量下载完成")
