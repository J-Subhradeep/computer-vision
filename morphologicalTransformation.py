# erosion and dilation
import cv2
import numpy as np

img = cv2.imread("resources/colorBalls.png", 0)
cv2.imshow("Image", img)


# erosion
_,mask = cv2.threshold(img,215,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5,),np.uint8)

e = cv2.erode(mask,kernel)


# dilation 
kernel = np.ones((3,3),np.uint8)
d = cv2.dilate(mask,kernel)
cv2.imshow("Dilate",d)

cv2.imshow("MASK",mask)
cv2.imshow("erotion",e)
cv2.waitKey()
cv2.destroyAllWindows()
