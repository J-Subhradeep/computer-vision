import cv2 as c
import numpy as np
def draw(event,x,y,flags,param):
    if event == c.EVENT_LBUTTONDBLCLK:
        c.circle(param,(x,y),100,(125,0,255),5)

c.namedWindow("res")
img = np.zeros((512,512,3), np.uint8)
c.setMouseCallback("res",draw,param=img)
while True:
    c.imshow("res",img)
    if c.waitKey(1) & 0xFF == ord("q"):
        break
c.destroyAllWindows()