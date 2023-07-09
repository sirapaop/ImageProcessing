import cv2 as cv
import numpy as np

img = cv.imread('filter/bot.jpg', cv.IMREAD_GRAYSCALE)
img = cv.resize(img,(600,600))

size = 5  
motion_blur_kernel = np.zeros((size, size))

motion_blur_kernel = np.eye(3, dtype=np.float32) #ทะแยงซ้ายไปขวา

# for i in range(size):
#     motion_blur_kernel[i, size - 1 - i] =  0.3  #ทะแยงขวาไปซ้าย

print(motion_blur_kernel)

output = cv.filter2D(img, -1, motion_blur_kernel)
cv.imshow('Motion_Blur Image', output)
cv.waitKey(0)
cv.destroyAllWindows()