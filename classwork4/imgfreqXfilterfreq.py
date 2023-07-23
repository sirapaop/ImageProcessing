import cv2 as cv
import numpy as np

img = cv.imread("./classwork4/paimon.jpg", cv.IMREAD_GRAYSCALE)
img = cv.resize(img,(800,600))

filter_h = 3
filter_w = 3
filter = np.zeros([filter_h, filter_w], dtype = np.float32)
filter[0,0] = 1; filter[0,1] = 0; filter[0,2] = -1;
filter[1,0] = 2; filter[1,1] = 0; filter[1,2] = -2; 
filter[2,0] = 1; filter[2,1] = 0; filter[2,2] = -1;

padding = np.pad(filter, [(0, img.shape[0]-3), (0, img.shape[1]-3)], mode='constant')
freq = np.fft.fft2(padding)
imgF = np.fft.fft2(img)

conclusion = freq * imgF

conclusion_inverse = np.fft.ifft2(conclusion)
output = np.real(conclusion_inverse)
imgMag_conclusion = cv.normalize(output, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)


sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize = 3)
imgMag_sobelx = cv.normalize(sobelx, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

picture = cv.hconcat([imgMag_sobelx, imgMag_conclusion])
cv.imshow("imgFreq x filterFreq", picture)
cv.waitKey(0)
cv.destroyAllWindows()
