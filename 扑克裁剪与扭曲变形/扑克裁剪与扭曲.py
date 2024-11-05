import cv2
import numpy as np
from PIL import Image


def crop_and_warp_parallelograms(image_path, polygons):
    try:
        # 打开图片文件
        img = Image.open(image_path)
        width, height = img.size
        print(f"Original image size: {width}x{height}")

        # 遍历每个平行四边形
        for i, polygon in enumerate(polygons):
            # 确保所有顶点坐标都是整数
            polygon = [(int(x), int(y)) for x, y in polygon]

            # 将PIL图像转换为OpenCV格式
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

            # 定义源点和平行四边形的四个角点
            src_pts = np.float32(polygon)

            # 计算平行四边形的边界框
            x_min, y_min = np.min(src_pts, axis=0).astype(int)
            x_max, y_max = np.max(src_pts, axis=0).astype(int)

            # 定义目标矩形的四个角点
            dst_pts = np.float32([[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]])

            # 计算透视变换矩阵
            M = cv2.getPerspectiveTransform(src_pts, dst_pts)

            # 应用透视变换
            warped_img = cv2.warpPerspective(img_cv, M, (width, height))

            # 裁剪出变换后的矩形区域
            cropped_warped_img = warped_img[y_min:y_max, x_min:x_max]

            # 保存裁剪后的图片到当前目录
            output_filename = f'warped_parallelogram_{i + 1}.jpg'
            cv2.imwrite(output_filename, cropped_warped_img)
            print(f"Saved: {output_filename}")

        print("所有图片已处理完成。")
    except Exception as e:
        print(f"发生错误: {e}")


# 平行四边形顶点列表
polygons = [
    [(57, 330), (340, 270), (400, 580), (80, 630)],  # a
    [(530, 140), (770, 180), (670, 460), (400, 410)],  # b
    [(775, 106), (1017, 82), (1115, 330), (845, 358)],  # c
    [(739, 387), (1022, 437), (986, 695), (646, 695)]  # d
]

# 图片路径
image_path = '作业.png'

# 调用函数
crop_and_warp_parallelograms(image_path, polygons)