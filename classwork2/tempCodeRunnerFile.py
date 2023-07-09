import cv2 as cv
import numpy as np

img = cv.imread('classwork2/Circle Objects.png' , cv.IMREAD_GRAYSCALE)


cv.circle(img, (0,0), 100, (0,255,0), -1)
# output = cv.filter2D(img, -1, filter_motionblur)

#cv.imwrite('filter/motion_output.png', output)
cv.imshow('circle Image', img)
cv.waitKey(0)
cv.destroyAllWindows()