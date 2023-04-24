import cv2
import numpy as np
img = cv2.imread("resources/image.jpg")
img1 = cv2.imread("resources/thor.jpg")
img = cv2.resize(img,(500,700))
img1 = cv2.resize(img1,(500,700))

# res = cv2.add(img1, img)

res = cv2.addWeighted(img,0.4,img1,0.6,0)
cv2.imshow("Image",res)
cv2.imshow("Image1",img)
cv2.imshow("Image2",img1)

cv2.waitKey()
cv2.destroyAllWindows()