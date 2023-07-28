import cv2 as cv
import numpy as np

img = cv.imread("./filter/bot.jpg", cv.IMREAD_GRAYSCALE)
img = cv.resize(img,(600,600))
ksize = (31,31)
sigmax = 2.5
output = cv.GaussianBlur(img, ksize, sigmax, borderType= cv.BORDER_REFLECT)

cv.imwrite('filter/Gaussian_output.png', output)