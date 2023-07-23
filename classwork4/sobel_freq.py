import cv2 as cv
import numpy as np

img = cv.imread("./classwork4/paimon.jpg", cv.IMREAD_GRAYSCALE)

filter_h = 3
filter_w = 3
filter = np.zeros([filter_h, filter_w], dtype = np.float32)
filter[0,0] = 1; filter[0,1] = 0; filter[0,2] = -1;
filter[1,0] = 2; filter[1,1] = 0; filter[1,2] = -2; 
filter[2,0] = 1; filter[2,1] = 0; filter[2,2] = -1;

padding = np.pad(filter, [(0, img.shape[0]-3), (0, img.shape[1]-3)], mode='constant')

freq = np.fft.fft2(padding)
# Normalize the filter to 0-255 range for visualization

imgReal = np.real(freq)
imgIma = np.imag(freq)
imgMag = np.sqrt(imgReal**2 + imgIma**2)
imgMag = np.log(1+imgMag)
filter_img = cv.normalize(imgMag, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

# Display the filter image
cv.imshow("filter frequency", filter_img)
#cv.imwrite("classwork4/filter_freq.png", filter_img)
cv.waitKey(0)
cv.destroyAllWindows()
