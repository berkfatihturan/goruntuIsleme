import cv2


def blur(img_path, k_size):
    # get img
    img = cv2.imread(img_path)
    # apply average filter
    im1 = cv2.blur(img, k_size)
    # showing original and filtered img
    cv2.imshow("image", im1)
    cv2.waitKey(0)


path = "../stock_img.jpg"
kernel_size = (5, 5)
blur(img_path=path, k_size=kernel_size)
