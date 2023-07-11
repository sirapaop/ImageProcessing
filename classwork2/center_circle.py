import cv2 as cv
import numpy as np

image = cv.imread("classwork2/Circle Objects.png")
gray = cv.cvtColor(image, cv.IMREAD_GRAYSCALE)
blur = cv.medianBlur(gray,5)
edges = cv.Canny(blur,230,255)
for row in range(0,image.shape[0],3):
    for col in range(0,image.shape[1],3):
        pixel = edges[row, col]
        if pixel > 230:
            #print(pixel)
            radius = 60  
            cv.circle(image, (col, row), radius, (0, 255,0),1 )
            

cv.imshow("Circle", image)
cv.waitKey(0)
cv.destroyAllWindows()













