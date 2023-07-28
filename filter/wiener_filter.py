
import cv2
import numpy as np

def wiener_filter(img_blurred, kernel, noise_var):
    fft_img_blurred = np.fft.fft2(img_blurred)
    fft_kernel = np.fft.fft2(kernel, s=img_blurred.shape)
    epsilon = 1e-8
    inverse_filter = np.conj(fft_kernel) / (np.abs(fft_kernel) ** 2 + noise_var + epsilon)

    fft_img_restored = fft_img_blurred * inverse_filter
    img_restored = np.fft.ifft2(fft_img_restored).real

    return img_restored.astype(np.uint8)

if __name__ == '__main__':
    img_blurred = cv2.imread('filter/Gaussian_output.png', cv2.IMREAD_GRAYSCALE)  
    kernel = np.array([[1, 4, 6, 4, 1],
                       [4, 16, 24, 16, 4],
                       [6, 24, 36, 24, 6],
                       [4, 16, 24, 16, 4],
                       [1, 4, 6, 4, 1]], dtype=np.float32) / 256
    noise_variance = 1.0

    # Apply the Wiener filter
    restored_image = wiener_filter(img_blurred, kernel, noise_variance)

    # Display the original blurred image and the restored image side by side
    picture = cv2.hconcat([img_blurred, restored_image])
    cv2.imshow("blur & wiener", picture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()