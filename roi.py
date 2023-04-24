import cv2
import numpy as np


# read image
img = cv2.imread("resources/thor.jpg")
img = cv2.resize(img,(800,800))

''' region of interest'''

"""(320,50), (440,205)"""
roi = img[50:205,320:440]

#now passing data into image
img[50:205,441:561] = roi
img[50:205,199:319] = roi

cv2.imshow("Image", img)
cv2.waitKey()
cv2.destroyAllWindows()