import cv2


def gaussian_filter(image_path, kernel_size):
    # get img
    original_image = cv2.imread(image_path)

    # apply Gaussian filter
    blurred_image = cv2.GaussianBlur(original_image, (kernel_size, kernel_size), 0)

    # showing original and filtered img
    cv2.imshow("img", blurred_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
kernel_size = 5  # Filtre boyutu (5x5)
gaussian_filter(image_path, kernel_size)
