import cv2
import numpy as np

img = cv2.imread("resources/image.jpg")
cv2.resize(img, (600, 400))
img = cv2.line(img, (0, 0), (200, 200), (0, 0, 255), 5)
img = cv2.arrowedLine(img, (100, 0), (300, 200), (0, 0, 255), 5)
img = cv2.rectangle(img,(384,100),(510,180),(0,255,0),5)
img  = cv2.circle(img,(447,333),50,(200,21,0),cv2.FILLED)
#Import only if not previously imported

pts = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32)
 
# pts = pts.reshape((-1, 1, 2))
 
isClosed = True
 
# Blue color in BGR
color = (255, 0, 0)
 
# Line thickness of 2 px
thickness = 2
 
# Using cv2.polylines() method
# Draw a Blue polygon with
# thickness of 1 px
img = cv2.polylines(img, [pts],
                      isClosed, color, thickness)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
