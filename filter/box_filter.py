import cv2 as cv
import numpy as np

img = cv.imread("./filter/bot.jpg", cv.IMREAD_GRAYSCALE)

filterSize = 15;
kernel = np.ones((filterSize, filterSize), np.float32)/(filterSize**2)

output = cv.filter2D(img, -1, kernel, borderType = cv.BORDER_REFLECT)

#cv.imwrite('Averange [1] ./filter/input', img)
cv.imwrite('filter/box_output.png', output)