#Import only if not previously imported
import cv2
img = cv2.imread("resources/image.jpg")     #(flag = 0 or 1 or -1)
#Import only if not previously imported
print(img.shape)
print("No of pixels",img.size)
print("Datatype ",img.dtype)

# split
print(cv2.split(img))
b,g,r = cv2.split(img)
# cv2.imshow("blue",b)
# cv2.imshow("green",g)
# cv2.imshow("red",r)

mr1 = cv2.merge((r,g,b))
cv2.imshow("rgb",mr1)

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()