# map-tool

 第 1 部分：什么是“地图瓦片（Tile）

 第 2 部分：如何“从在线地图 API 获取瓦片”

 第 3 部分：如何把瓦片拼成一张大图？

 第 4 部分：如何把地图导出到 AutoCAD（DXF / DWG）

  第 5 部分 用户输入信息/地理计算 → 算出瓦片范围/下载瓦片/拼图（Tiles → Big Map）/生成 World File（地理参考文件）/导出 AutoCAD（DWG/DXF）

  ###Python：

计算瓦片范围 → 批量下载 → 拼接大图（PNG/TIF）
生成世界文件（.pgw/.tfw）
用 ezdxf 写出 DXF，把底图作为外部光栅附着（Underlay/Image）并按世界文件定位


批量转 DWG：

AutoCAD：脚本或手动打开 DXF → 另存为 DWG

map_to_dxf_tool/
│
├── main.py                       # 主入口：执行整个流程
│
├── config.py                     # 配置 (地图源、瓦片大小、输出路径)
│
├── downloader/
│   ├── __init__.py
│   ├── tile_calc.py              # 经纬度->瓦片坐标计算、瓦片范围计算
│   ├── tile_downloader.py        # 批量下载瓦片
│   ├── tile_stitcher.py          # 拼接瓦片成大图
│
├── geo/
│   ├── __init__.py
│   ├── worldfile.py              # 生成 .pgw/.tfw 世界文件
│   ├── coordinate.py             # 经纬度/投影/WebMercator 计算
│
├── dxf/
│   ├── __init__.py
│   ├── dxf_exporter.py           # 使用 ezdxf 生成 DXF + 插入图像 underlay
│
├── utils/
│   ├── __init__.py
│   ├── logger.py                 # 打印日志
│   ├── file_tools.py             # 创建目录、路径管理
│
├── output/                       # 输出目录：拼图、pgw、dxf 都放这里
│
└── requirements.txt              # pip 依赖

## how to use good AutoCAD
案 A：使用 OpenStreetMap（OSM）或 ArcGIS（合法 & 免费）

使用 MapTiler / Mapbox（有 API Key，商业允许）

非常大的区域（几千张瓦片以上），请使用 商业镜像服务（例如 MapTiler、OpenMapTiles）
