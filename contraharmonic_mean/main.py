import cv2
import numpy as np


def contraharmonic_mean_filter(image_path, filter_size, Q):
    # get img
    original_image = cv2.imread(image_path)

    # apply Contraharmonic mean filter
    filtered_image = cv2.filter2D(original_image, -1,
                                  np.ones((filter_size, filter_size), np.float32) ** (Q + 1) / np.ones(
                                      (filter_size, filter_size), np.float32) ** Q)

    # showing original and filtered img
    cv2.imshow(f'Contraharmonic Mean Filtre (Q={Q}, Filtre Boyutu: {filter_size}x{filter_size})',
               filtered_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
filter_size = 3
Q = 1

contraharmonic_mean_filter(image_path, filter_size, Q)
