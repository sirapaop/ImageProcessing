import cv2 as cv
import numpy as np
img_input = cv.imread("78022.jpg",cv.IMREAD_GRAYSCALE)

img_output = np.log(img_input)
img_max = np.max(img_output)
img_output = img_output * (0/img_max)

img_output = np.array(img_output, dtype = np.uint8)

#cv.imwrite("Demo03_DIY_img_input.png", img_input)
cv.imwrite("Demo03_DIY_img_output.png", img_output)