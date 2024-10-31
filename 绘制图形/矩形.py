import cv2
import numpy as np

# 创建一个空白图像
image = np.zeros((200, 320, 3), dtype=np.uint8) + 255  # 白色背景

# 定义起始位置、边缘间距和矩形增加的步长
start_pos = (10, 10)  # 起始位置
spacing = 10  # 边距和矩形间距离
step = 10  # 每个矩形增加的宽度和高度

# 固定颜色
color = (0,0,0)

# 使用循环来绘制多个矩形
for i in range(9):
    # 计算当前矩形的位置和尺寸
    rect_start = (start_pos[0] + spacing * i, start_pos[1] + spacing * i)
    rect_end = (rect_start[0] + 300 - spacing * i * 2, rect_start[1] + 180 - spacing * i * 2)

    # 绘制矩形
    cv2.rectangle(image, rect_start, rect_end, color, 2)

# 显示图像
cv2.imshow('嵌套矩形', image)
cv2.waitKey(0)
cv2.destroyAllWindows()