import cv2
import numpy as np


def contrast_stretching(image_path):
    # get img
    original_image = cv2.imread(image_path, 0)

    # calc max.min pixel value
    min_val, max_val, _, _ = cv2.minMaxLoc(original_image)

    # Contrast stretching
    stretched_image = np.uint8((original_image - min_val) * 255 / (max_val - min_val))

    # showing original and filtered img
    cv2.imshow('Kontrast Genişletilmiş Görüntü', stretched_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
contrast_stretching(image_path)
