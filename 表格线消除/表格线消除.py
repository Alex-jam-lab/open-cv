import cv2

# 读取图像
image = cv2.imread('line.jpg')

# 转换为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 应用二值化
thre = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# 定义水平结构元素
horizontal = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 1))

# 水平去除
remove = cv2.morphologyEx(thre, cv2.MORPH_OPEN, horizontal, iterations=2)

# 查找轮廓
cnts = cv2.findContours(remove, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# 绘制轮廓
for c in cnts:
    cv2.drawContours(image, [c], -1, (255, 255, 255), 5)

# 定义垂直结构元素
vertical = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 40))

# 垂直去除
remove_vertical = cv2.morphologyEx(thre, cv2.MORPH_OPEN, vertical, iterations=2)

# 查找轮廓
cnts = cv2.findContours(remove_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

# 绘制轮廓
for c in cnts:
    cv2.drawContours(image, [c], -1, (255, 255, 255), 5)

# 显示或保存处理后的图像
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()