import cv2 as cv
import numpy as np 



img = cv.imread("classwork3\salt&pepper_Image.jpg", cv.IMREAD_GRAYSCALE)

denoised_image = cv.medianBlur(img, 3)  

#cv2.imwrite('output_image.png', denoised_image)


cv.imshow('invert_Image', denoised_image)
cv.waitKey(0)
cv.destroyAllWindows()