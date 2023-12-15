import cv2
import numpy as np


def add_salt_and_pepper_noise(image_path, salt_prob, pepper_prob):
    # get img
    original_image = cv2.imread(image_path)

    # get size of img
    rows, cols, _ = original_image.shape

    # create a mask for add salt and pepper mask
    salt_mask = np.random.rand(rows, cols) < salt_prob
    pepper_mask = np.random.rand(rows, cols) < pepper_prob

    # add salt and pepper noise
    original_image[salt_mask] = 255
    original_image[pepper_mask] = 0

    # showing original and filtered img
    cv2.imshow(f'Salt and Pepper Gürültüsü Eklenmiş Görüntü\nSalt Prob: {salt_prob}, Pepper Prob: {pepper_prob}',
               original_image)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
salt_probability = 0.02
pepper_probability = 0.02

add_salt_and_pepper_noise(image_path, salt_probability, pepper_probability)
