
import cv2 as cv
import numpy as np

# 创建一个400x400的白色背景图像
img = np.ones((400, 400, 3), dtype=np.uint8) * 255

# 定义箭靶的中心点
center = (200, 200)

# 绘制同心圆
radius_start = 150
radius_step = 30
colors = [(0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255)]
for i, color in enumerate(colors):
    radius = radius_start - i * radius_step
    cv.circle(img, center, radius, color, thickness=-1)

# 添加最内层的实心黑圆
inner_radius = 30
cv.circle(img, center, inner_radius, (0, 0, 0), thickness=-1)

# 在箭靶的右侧放置数字
right_labels = ['6', '7', '8', '9']
label_position_right = [320, 290, 260, 230]
label_font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
label_scale = 1
label_thickness = 2
label_color = (0, 0, 255)

# 右侧数字的放置
for label, position in zip(right_labels, label_position_right):
    cv.putText(img, label, (position, 197), label_font, label_scale, label_color, label_thickness, cv.LINE_AA)

# 在箭靶的左侧放置数字
left_labels = ['9', '8', '7', '6']  # 假设这是您要添加到左侧的数字
label_position_left = [150,120, 90, 60]

# 左侧数字的放置
for label, position in zip(left_labels, label_position_left):
    cv.putText(img, label, (position, 197), label_font, label_scale, label_color, label_thickness, cv.LINE_AA)

# 绘制十字线
crosshair_thickness = 2
cv.line(img, center, (30, center[1]), (255, 0, 0), crosshair_thickness)
cv.line(img, center, (370, center[1]), (255, 0, 0), crosshair_thickness)
cv.line(img, center, (center[0], 30), (255, 0, 0), crosshair_thickness)
cv.line(img, center, (center[0], 370), (255, 0, 0), crosshair_thickness)

# 显示图像
cv.namedWindow('draw_circle')
cv.imshow('draw_circle', img)
cv.waitKey(0)
cv.destroyAllWindows()