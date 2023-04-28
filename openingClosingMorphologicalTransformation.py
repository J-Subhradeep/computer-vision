import cv2
import numpy as np

# opening is justno another name of erosion followed by dilation
img = cv2.imread("resources/colorBalls.png", 0)
_,mask = cv2.threshold(img,215,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((3,3),np.uint8)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
c= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
cv2.imshow("Img",img)
cv2.imshow("kernel",kernel)
cv2.imshow("mask",mask)
cv2.imshow("opening",o)
cv2.imshow("Closing",c)
cv2.waitKey()
cv2.destroyAllWindows()