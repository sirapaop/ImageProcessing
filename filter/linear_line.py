import cv2 as cv 

img = cv.imread("./filter/bot.jpg", cv.IMREAD_GRAYSCALE)
# 1774/2364
start_p = (0,0)
end_p = (1000, 2000)
color = (255,250,255)
thick = 9

output = cv.line(img, start_p, end_p, color, thick)

cv.imwrite('filter/line_output.png', output)