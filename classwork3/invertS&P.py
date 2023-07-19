import cv2 as cv
import numpy as np 

img = cv.imread("classwork3\salt&pepper_Image.jpg", cv.IMREAD_GRAYSCALE)

for i in range(3,13,2):
    denoised_image = cv.medianBlur(img, i) 
    print(i) 
    cv.imshow('invert_Image', denoised_image)

cv.imshow('P&S_Image', img)  
cv.waitKey(0)
cv.destroyAllWindows()