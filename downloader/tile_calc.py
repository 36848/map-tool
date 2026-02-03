import math

def latlon_to_tile(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2 ** zoom

    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.log(math.tan(lat_rad) + 1/math.cos(lat_rad)) / math.pi) / 2.0 * n)

    return x_tile, y_tile


def calculate_tile_range(lat, lon, zoom, half_range=1):
    """
    保留你原来的 3x3 / 5x5 结构
    """
    cx, cy = latlon_to_tile(lat, lon, zoom)

    return {
        "zoom": zoom,
        "min_x": cx - half_range,
        "max_x": cx + half_range,
        "min_y": cy - half_range,
        "max_y": cy + half_range
    }


def bbox_to_tile_range(min_lon, min_lat, max_lon, max_lat, zoom):
    """
    新增：支持按地理范围下载
    """

    x1, y1 = latlon_to_tile(max_lat, min_lon, zoom)  # 左上
    x2, y2 = latlon_to_tile(min_lat, max_lon, zoom)  # 右下

    return {
        "zoom": zoom,
        "min_x": min(x1, x2),
        "max_x": max(x1, x2),
        "min_y": min(y1, y2),
        "max_y": max(y1, y2)
    }