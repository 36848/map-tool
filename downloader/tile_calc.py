import math

def latlon_to_tile(lat, lon, zoom):
    """
    将经纬度转换为 XYZ 瓦片坐标（Web Mercator 标准公式）
    """
    lat_rad = math.radians(lat)
    n = 2 ** zoom

    x_tile = int((lon + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2.0 * n)

    return x_tile, y_tile


def calculate_tile_range(lat, lon, zoom, half_range=1):
    """
    给定一个中心点，经纬度 -> 计算周围瓦片范围.
    
    参数：
        lat, lon  : 中心经纬度
        zoom      : 地图缩放级别
        half_range: 下载范围（例如 1=3x3, 2=5x5）

    返回：
        字典 {min_x, max_x, min_y, max_y, zoom}
    """
    center_x, center_y = latlon_to_tile(lat, lon, zoom)

    min_x = center_x - half_range
    max_x = center_x + half_range
    min_y = center_y - half_range
    max_y = center_y + half_range

    return {
        "zoom": zoom,
        "min_x": min_x,
        "max_x": max_x,
        "min_y": min_y,
        "max_y": max_y
    }
