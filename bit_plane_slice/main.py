from PIL import Image
import numpy as np


def bit_plane_slice(image_path, bit_plane):
    # get img
    image = Image.open(image_path)
    img_array = np.array(image)
    height, width = img_array.shape[:2]
    mask = 2 ** bit_plane
    sliced_image = np.bitwise_and(img_array, mask)
    sliced_image = Image.fromarray(sliced_image)

    # showing original and filtered img
    image.show()
    sliced_image.show()


image_path = "../stock_img.jpg"
bit_plane = 7
bit_plane_slice(image_path, bit_plane)
