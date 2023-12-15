import cv2
import numpy as np


def gamma_correction(image_path, gamma):
    #get img
    original_image = cv2.imread(image_path)

    # normalize the piksel value
    image_normalized = original_image / 255.0

    # apply gamma correction
    corrected_image = np.power(image_normalized, gamma)
    corrected_image = (corrected_image * 255).astype(np.uint8)

    # showing original and filtered img
    cv2.imshow('Gamma Düzeltme'.format(gamma), corrected_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
gamma_value = 2.0
gamma_correction(image_path, gamma_value)
