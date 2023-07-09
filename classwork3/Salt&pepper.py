import cv2 as cv
import random
img = cv.imread("classwork3/anya.jpg", cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

#set number of white pixel (salt)
number_of_white_pixel = int(density_salt * (img.shape[0]*img.shape[1]))

# add salt to the image
for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 255

# set number of black pixcel (pepper)
number_of_black_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

#add pepper to the img
for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 0

#cv.imwrite('classwork3/salt&pepper_Image.jpg', img)
cv.imshow('salt&pepper Image', img)
cv.waitKey(0)
cv.destroyAllWindows()