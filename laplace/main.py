import cv2

# get img
img = cv2.imread('../stock_img.jpg', cv2.IMREAD_GRAYSCALE)

# apply Laplacian filter
laplacian_img = cv2.Laplacian(img, cv2.CV_8U)

# showing original and filtered img
cv2.imshow("img",laplacian_img)
cv2.waitKey(0)
