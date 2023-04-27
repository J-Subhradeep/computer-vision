import cv2
import numpy as np
img = cv2.imread("resources/image.jpg")
img1 = cv2.imread("resources/thor.jpg")
img = cv2.resize(img,(500,700))
img1 = cv2.resize(img1,(500,700))
imgZero = np.zeros((500,700,3),np.uint8)
cv2.namedWindow("win") # create track bar windows
def blend(x):
    pass
cv2.createTrackbar("alpha","win",1,100,blend)
switch = "0 : OFF \n 1: ON" # create switch for invoke the trackbars
cv2.createTrackbar(switch,"win",0,1,blend)

# res = cv2.add(img1, img)
while True:
    s = cv2.getTrackbarPos(switch,"win")
    a = cv2.getTrackbarPos("alpha","win")
    n = float(a/100)
    if not s:
        res = img[:]
    else:
        res = cv2.addWeighted(img,1-n,img1,n,0)
        cv2.putText(res, str(a),(20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    cv2.imshow("result",res)
    if cv2.waitKey(1) == ord("q"):
        break


cv2.destroyAllWindows()