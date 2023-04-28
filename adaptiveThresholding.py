import cv2
import numpy as np

img = cv2.imread("resources/colorBalls.png",0)

cv2.imshow("Image",img)
th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("Res",th2)
cv2.waitKey()
cv2.destroyAllWindows()