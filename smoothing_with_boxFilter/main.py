import cv2


def box_filter(image_path, kernel_size):
    # get img
    original_image = cv2.imread(image_path)

    # apply box filter
    smoothed_image = cv2.boxFilter(original_image, -1, (kernel_size, kernel_size))

    # showing original and filtered img
    cv2.imshow('img', smoothed_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
kernel_size = 25

box_filter(image_path, kernel_size)
