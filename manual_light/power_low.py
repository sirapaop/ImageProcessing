import cv2 as cv
import numpy as np

img_in = cv.imread("manual_light\light.jpg",cv.IMREAD_GRAYSCALE)

gamma = 4
gamma_corrected = (img_in/255)**gamma
gamma_corrected = gamma_corrected*255

img_out = np.array(gamma_corrected, dtype= "uint8")
cv.imshow("power_low",img_out)

cv.imwrite("manual_light\pow_low_input.png", img_in)
cv.imwrite("manual_light\pow_low_output.png", img_out)