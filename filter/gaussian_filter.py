import cv2 as cv
import numpy as np

img = cv.imread("./filter/bot.jpg", cv.IMREAD_GRAYSCALE)

ksize = (31,31)
sigmax = 5.0
output = cv.GaussianBlur(img, ksize, sigmax, borderType= cv.BORDER_REFLECT)

cv.imwrite('filter/Gaussian_output.png', output)