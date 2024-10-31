import cv2 as cv
import numpy as np

img = np.zeros((200, 360, 3), dtype=np.uint8) + 255

# 绘制等轴椭圆起始点绘制四分之一圆角
cv.ellipse(img, (50, 50), (20, 20), 0, 180, 270, (0, 0, 0), 2)
cv.ellipse(img, (270, 50), (20, 20), 0, 270, 360, (0, 0, 0), 2)
cv.ellipse(img, (270, 110), (20, 20), 0, 0, 90, (0, 0, 0), 2)
cv.ellipse(img, (50, 110), (20, 20), 0, 90, 180, (0, 0, 0), 2)

# 绘制直线
cv.line(img, (50, 30), (270, 30), (0, 0, 0), 2)
cv.line(img, (290, 50), (290, 110), (0, 0, 0), 2)
cv.line(img, (270, 130), (50, 130), (0, 0, 0), 2)
cv.line(img, (30, 110), (30, 50), (0, 0, 0), 2)

# 显示图像
cv.imshow('rectangle', img)
cv.waitKey(0)