import cv2 as cv
import numpy as np

img_in = cv.imread("manual_light\dark.jpg",cv.IMREAD_COLOR)

gamma = 1
gamma_corrected = (img_in/100)**gamma
gamma_corrected = gamma_corrected*255

img_out = np.array(gamma_corrected, dtype= "uint8")
cv.imshow("power_law",img_out)

cv.imwrite("manual_light\pow_high_input.png", img_in)
cv.imwrite("manual_light\pow_high_output.png", img_out)