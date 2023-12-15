import cv2
import numpy as np
from matplotlib import pyplot as plt


def histogram(img_path):
    # get img
    img = cv2.imread(img_path, 0)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()

    # showing original and filtered img
    plt.plot(cdf_normalized, color="b")
    plt.hist(img.flatten(), 256, [0, 256], color="r")
    plt.xlim([0, 256])
    plt.legend(("cdf", "histogram"), loc="upper left")
    plt.show()


img_path = "../stock_img.jpg"
histogram(img_path=img_path)
