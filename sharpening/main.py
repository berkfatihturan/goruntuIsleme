import cv2


def apply_sharpening(image_path, ksize=3, sigma=1.0):
    # get img
    original_image = cv2.imread(image_path)

    # sharpening
    blurred_image = cv2.GaussianBlur(original_image, (ksize, ksize), sigma)
    sharpened_image = cv2.Laplacian(blurred_image, cv2.CV_8U, ksize=ksize)

    # showing original and filtered img
    cv2.imshow('Sharpening Result', sharpened_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
k_size = 3
sigma = 1.0
apply_sharpening(image_path, ksize=k_size, sigma=sigma)
