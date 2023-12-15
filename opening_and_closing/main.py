import cv2
import numpy as np


def apply_opening(image_path, kernel_size):
    # get img
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # apply opening (Erozyon + Genişleme)
    kernel_opening = np.ones((kernel_size, kernel_size), np.uint8)
    opening_result = cv2.morphologyEx(original_image, cv2.MORPH_OPEN, kernel_opening)

    # showing original and filtered img
    cv2.imshow('opening_result', opening_result)
    cv2.waitKey(0)


def apply_closing(image_path, kernel_size):
    # get img
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # apply_closing (Genişleme + Erozyon)
    kernel_closing = np.ones((kernel_size, kernel_size), np.uint8)
    closing_result = cv2.morphologyEx(original_image, cv2.MORPH_CLOSE, kernel_closing)

    # showing original and filtered img
    cv2.imshow('closing_result', closing_result)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
kernel_size_opening = 3
kernel_size_closing = 3

apply_opening(image_path, kernel_size=kernel_size_opening)
apply_closing(image_path, kernel_size=kernel_size_closing)
