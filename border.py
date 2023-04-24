import cv2
import numpy as np

img = cv2.imread("resources/image.jpg")
img = cv2.copyMakeBorder(img,10,10,5,5,cv2.BORDER_CONSTANT,value=(255,0,0))
cv2.imshow("Image",img)
cv2.waitKey()
cv2.destroyAllWindows()