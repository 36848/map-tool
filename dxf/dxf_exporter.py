import ezdxf
from PIL import Image
import os

def export_dxf(image_path, worldfile_path, out_path):

    # 读取世界文件
    vals = open(worldfile_path).read().strip().split("\n")
    A, D, B, E, C, F = map(float, vals)

    # 图像像素
    w, h = Image.open(image_path).size

    width_m  = w * A
    height_m = h * (-E)

    # DXF 中图像插入点 = 左下角
    insert_x = C
    insert_y = F - height_m

    doc = ezdxf.new("R2010")
    doc.header["$INSUNITS"] = 6  # 米

    msp = doc.modelspace()

    # 修改这里！！！！！
    image_def = doc.add_image_def(
        os.path.abspath(image_path),
        size_in_pixel=(w, h)     # ✔ 正确名称
    )

    msp.add_image(
        image_def,
        insert=(insert_x, insert_y),
        size_in_units=(width_m, height_m),
        rotation=0
    )

    doc.saveas(out_path)
    print(f"[OK] DXF 输出：{out_path}")