import cv2
import numpy as np
img = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img,(150,100),(200,250),(255,255,255),-1)
img2 = np.zeros((250,500,3),np.uint8)
img2 = cv2.rectangle(img2, (10,10),(170,190),(255,255,255),-1)

cv2.imshow("Image 1",img1)
cv2.imshow("Image 2",img2)

bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2) 
cv2.imshow("AND",bitAnd)
cv2.imshow("OR",bitOr)
cv2.waitKey(0)
cv2.destroyAllWindows()
