import cv2 as cv
import numpy as np

image = cv.imread("classwork2/Circle Objects.png", cv.IMREAD_GRAYSCALE)

black_image = np.zeros_like(image)

for row in range(image.shape[0]):
    for col in range(image.shape[1]):
        pixel = image[row, col]
        if pixel > 230:
            #print(pixel)
            radius = 50  
            cv.circle(black_image, (col, row), radius, (255, 255, 255),1 )
            

cv.imshow("Circle", black_image)
cv.waitKey(0)
cv.destroyAllWindows()













