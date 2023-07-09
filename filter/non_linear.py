import cv2 as cv
import numpy as np

img = cv.imread("filter/bot.jpg", cv.IMREAD_GRAYSCALE)
img = cv.resize(img,(600,600))

output = cv.medianBlur(img, 5)

cv.imshow('Non_linear img', output)
cv.waitKey(0)
cv.destroyAllWindows()
