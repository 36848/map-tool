from downloader.tile_calc import calculate_tile_range
from downloader.tile_downloader import download_tiles
from downloader.tile_stitcher import stitch_tiles
from geo.worldfile import make_worldfile
from dxf.dxf_exporter import export_dxf

lat = 53.989
lon = -7.360
zoom = 19

tile_range = calculate_tile_range(lat, lon, zoom, half_range=1)

download_folder = "D:/maptool/tiles"

download_tiles(tile_range, download_folder)

merged_path, tile_info = stitch_tiles(download_folder, "D:/maptool/output/map.png")

wld_path = make_worldfile(merged_path, tile_info, zoom)

export_dxf(merged_path, wld_path, "D:/maptool/output/map.dxf")

print("\n 完成！现在打开 AutoCAD → 打开 map.dxf → 另存为 DWG")
