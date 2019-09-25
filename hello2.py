import cv2
import numpy as np
import matplotlib.pyplot as plt 

def to_canny(image):
    gray=cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,150,150)
    return canny
image=cv2.imread("img.jpeg")
lane_image=np.copy(image)
canny=to_canny(lane_image)
plt.imshow(image)
plt.imshow(canny)
plt.show()
