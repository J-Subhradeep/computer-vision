import cv2
import numpy as np

img1 = cv2.imread("resources/image.jpg")
img2 = cv2.imread("resources/wapon.jpg")

print(img1.shape, img2.shape)

r, c, ch = img2.shape
# roi creation

roi = img1[0:r, 0:c]

img_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_,mask = cv2.threshold(img_gray,230, 255, cv2.THRESH_BINARY_INV)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
mask = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
res = cv2.add(img1_bg,img2_fg)
final = img1
final[0:r,0:c] = res

cv2.imshow("Image gray", img_gray)
cv2.imshow("Threshold",mask)
cv2.imshow("MASK fg",img2_fg)
cv2.imshow("Img 1 bg",img1_bg)
cv2.imshow("ADD",res)
cv2.imshow("Final result",final)
cv2.waitKey()
cv2.destroyAllWindows()
