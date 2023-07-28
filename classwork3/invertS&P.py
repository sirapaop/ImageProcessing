import cv2 as cv
from skimage.metrics import structural_similarity as ssim

img = cv.imread("classwork3/salt&pepper_Image.jpg", cv.IMREAD_GRAYSCALE)
img = cv.resize(img, (900, 700))
denoised_image = cv.medianBlur(img, 9)

original_image = cv.imread("classwork3/anya.jpg", cv.IMREAD_GRAYSCALE)
original_image = cv.resize(original_image, (900, 700))

ssim_score = ssim(original_image, denoised_image)
print("median_blur ขนาด 9")
print(f'คะแนน SSIM: {ssim_score}')

picture = cv.hconcat([original_image, denoised_image])
#cv.imwrite('classwork3/inverst3.png', denoised_image)
cv.imshow("salt&pepper x invert_Image", picture)
cv.waitKey(0)
cv.destroyAllWindows()

