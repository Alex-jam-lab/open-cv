import cv2
import numpy as np

# 打开摄像头
cap = cv2.VideoCapture(0)

# 获取摄像头的分辨率
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置视频的尺寸为摄像头分辨率的一半
half_width = width // 2
half_height = height // 2

# 初始化截图计数器
frame_count = 0
video_count = 0
is_recording = False

# 定义视频编码器
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # 将帧缩小至一半
    resized_frame = cv2.resize(frame, (half_width, half_height))

    # 转换为 HSV 格式以便于颜色过滤
    hsv = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)

    # 定义蓝色范围
    lower_blue = np.array([90, 50, 50])  # 蓝色的下界
    upper_blue = np.array([130, 255, 255])  # 蓝色的上界

    # 创建掩膜
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 使用形态学操作去除噪声
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # 只保留蓝色区域
    blue_object = cv2.bitwise_and(resized_frame, resized_frame, mask=mask)

    # 扩大显示窗口的大小
    display_frame = cv2.resize(blue_object, (width, height))

    # 显示结果
    cv2.imshow('Blue Object', display_frame)

    # 检测键盘输入
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # 按 'q' 键退出循环
        break
    elif key == ord('s'):  # 按 's' 键截一张图
        cv2.imwrite(f'image_{frame_count}.png', blue_object)  # 保存掩膜后的图像
        frame_count += 1
        print(f"已保存当前帧为 image_{frame_count - 1}.png")
    elif key == ord('r'):  # 按 'r' 键开始/结束录制视频
        if not is_recording:
            # 开始录制视频
            video_writer = cv2.VideoWriter(f'video_{video_count}.mp4', fourcc, 20.0, (half_width, half_height))
            print("开始录制视频...")
            is_recording = True
        else:
            # 结束录制视频
            video_writer.release()
            video_count += 1
            print(f"已保存视频为 video_{video_count - 1}.mp4")
            is_recording = False

    if is_recording:
        # 写入当前帧到视频文件
        video_writer.write(blue_object)

# 释放资源并关闭窗口
cap.release()
if is_recording:
    video_writer.release()
cv2.destroyAllWindows()