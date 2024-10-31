

import cv2
import numpy as np

# 创建一个空白图像
img = np.zeros((600, 600, 3), dtype=np.uint8) + 255  # 创建一个白色背景的图像

# 顶点坐标
vertex_top = (300, 500)  # 顶点位于下方
vertex_left = (150, 200)  # 左侧顶点
vertex_right = (450, 200)  # 右侧顶点

# 使用cv2.line()绘制三条边
cv2.line(img, vertex_top, vertex_left, (0, 0, 0), 2)  # 从顶点到底部左侧
cv2.line(img, vertex_top, vertex_right, (0, 0, 0), 2)  # 从顶点到底部右侧
cv2.line(img, vertex_left, vertex_right, (0, 0, 0), 2)  # 连接底部两侧

# 显示图像
cv2.imshow("Triangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


