import cv2 as cv
import numpy as np

# กำหนดขนาดและทิศทางของ Motion Blur
kernel_size = 3
angle = 60

# สร้างเมตริกซ์ว่างที่มีขนาด kernel_size x kernel_size
kernel = np.zeros((kernel_size, kernel_size))

# คำนวณตำแหน่งศูนย์กลางของเมตริกซ์
center = (kernel_size - 1) / 2

# คำนวณค่าสำหรับทิศทางและระยะที่จะสร้าง Motion Blur
theta = np.radians(angle)
distance = int((kernel_size - 1) / 2)

# กำหนดค่าสำหรับ Motion Blur ในเมตริกซ์
for i in range(kernel_size):
    for j in range(kernel_size):
        x = i - center
        y = j - center
        if np.abs(np.sin(theta) * x - np.cos(theta) * y) <= distance:
            kernel[i, j] = 1 / (2 * distance + 1)

# โหลดภาพ
image = cv.imread('filter/bot.jpg')
image = cv.resize(image,(600,600))

# กรองภาพโดยใช้ Motion Blur
blurred_image = cv.filter2D(image, -1, kernel)

# แสดงผลลัพธ์
cv.imshow('Motion Blur Image', blurred_image)
cv.waitKey(0)
cv.destroyAllWindows()
