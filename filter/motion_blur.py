import cv2 as cv
import numpy as np

img = cv.imread('filter/bot.jpg')
img = cv.resize(img,(600,600))

size = 20

filter_motionblur = np.zeros((size, size))
filter_motionblur[int((size-1)/2), :] = np.ones(size)
filter_motionblur = filter_motionblur / size

output = cv.filter2D(img, -1, filter_motionblur)

#cv.imwrite('filter/motion_output.png', output)
cv.imshow('Motion_Blur Image', output)
cv.waitKey(0)
cv.destroyAllWindows()




