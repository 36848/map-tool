from downloader.tile_calc import calculate_tile_range
from downloader.tile_downloader import download_tiles
from downloader.tile_stitcher import stitch_tiles

lat = 53.989
lon = -7.360
zoom = 15

tile_range = calculate_tile_range(lat, lon, zoom, half_range=1)

# 自定义保存位置（你想放哪里都可以）
download_folder = "D:/cccc"

# 下载瓦片
download_tiles(tile_range, download_folder)

# 拼接大图
stitch_tiles(download_folder, "D:/cccc/output/map.png")