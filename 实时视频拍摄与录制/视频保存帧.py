import cv2
import numpy as np

# 打开视频文件
cap = cv2.VideoCapture('redone.mp4')

# 获取视频的帧率和尺寸
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = 500
frame_height = 800

# 创建 VideoWriter 对象用于输出视频
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('aaa.avi', fourcc, fps, (frame_width, frame_height))

frame_count = 0  # 记录保存的帧数

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([155, 43, 46])
        upper = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv, lower, upper)
        frame = cv2.bitwise_and(frame, frame, mask=mask1)

        cv2.imshow('frame', frame)

        # 检测键盘输入
        key = cv2.waitKey(20) & 0xFF
        if key == ord('q'):  # 按 'q' 键退出循环
            break
        elif key == ord('s'):  # 按 's' 键开始连续保存帧
            print("开始连续保存帧...")
            while True:
                ret, frame = cap.read()
                if ret:
                    frame = cv2.resize(frame, (frame_width, frame_height))
                    cv2.imshow('frame', frame)

                    # 保存当前帧
                    cv2.imwrite(f'frame_{frame_count}.jpg', frame)
                    frame_count += 1

                    # 等待用户按下其他键
                    key = cv2.waitKey(20) & 0xFF
                    if key != ord('s'):  # 如果不是 's' 键，则退出保存循环
                        break
            print("停止保存帧...")
        else:
            frame = cv2.resize(frame, (frame_width, frame_height))
            out.write(frame)
    else:
        break

# 释放资源并关闭窗口
cap.release()
out.release()
cv2.destroyAllWindows()