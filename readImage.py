import cv2
image = cv2.imread(r"resources\image.jpg")
print(image.shape)
image = cv2.resize(image,(700,433))
cv2.imshow("Original",image)



# read in grayscale

image = cv2.imread(r"resources\image.jpg",0)
print(image.shape)
image = cv2.resize(image,(700,433))
cv2.imshow("grayscale",image)
cv2.waitKey()
cv2.destroyAllWindows()