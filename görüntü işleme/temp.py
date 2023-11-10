import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("indir.jpg", 0)

img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

plt.figure()
plt.plot(img_hist)
plt.show()