import cv2
import numpy as np


def apply_sobel_filter(img_path):
    # get img
    original_image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # apply Sobel filter X and Y direction
    sobel_x = cv2.Sobel(original_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(original_image, cv2.CV_64F, 0, 1, ksize=3)

    # Get absolute value of Sobel gradients for calculate magnitude
    magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)

    # showing original and filtered img
    cv2.imshow('Original', original_image)
    cv2.imshow('Sobel Filtresi (X)', sobel_x)
    cv2.imshow('Sobel Filtresi (Y)', sobel_y)
    cv2.imshow('Magnitude', magnitude)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
apply_sobel_filter(image_path)
