import cv2


def split_rgb(image_path):
    # get img
    original_image = cv2.imread(image_path, )

    # split the img to r,g,b
    r_channel, g_channel, b_channel = cv2.split(original_image)

    # showing original and filtered img
    cv2.imshow(f'original', original_image)
    cv2.imshow(f'red', r_channel)
    cv2.imshow(f'green', g_channel)
    cv2.imshow(f'blue', b_channel)
    cv2.waitKey(0)


image_path = '../stock_img.jpg'
split_rgb(image_path)
