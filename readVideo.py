import cv2
cap = cv2.VideoCapture("resources/video.mp4")
while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(800,433))
    frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("frame2",frame2)
    k = cv2.waitKey(25)
    if k==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()