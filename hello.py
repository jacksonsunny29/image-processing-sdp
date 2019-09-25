#using canny


import cv2
import numpy as np

image=cv2.imread("img.jpeg")
lane_image=np.copy(image)
gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
canny=cv2.Canny(blur,150,150)
cv2.imshow("input",gray)
cv2.imshow("result",canny)
cv2.waitKey(0)
