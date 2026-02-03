# config.py

# 当前使用哪个地图源（可选： "OSM", "ArcGIS", "MapTiler"）
MAP_SOURCE = "ArcGIS"     



# 统一定义所有可用的 XYZ URL 模板
MAP_SOURCES = {
    "OSM": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",

    # ArcGIS （注意 ArcGIS 使用 {z}/{y}/{x} 顺序！）
    "ArcGIS": "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
}

# OSM 礼仪要求
USER_AGENT = "MapTool/1.0 (yu.xia@tmdesign.ie)"
