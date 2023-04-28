import cv2
import numpy as np

img = cv2.imread("resources/colorBalls.png",0)


cv2.imshow("Image", img)

_,th1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,100,255,cv2.THRESH_TOZERO)

cv2.imshow("Image 2",th1)
cv2.imshow("Image 3",th2)
cv2.imshow("Image 4",th3)
cv2.waitKey()
cv2.destroyAllWindows()

