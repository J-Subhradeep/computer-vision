import cv2
cap  = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter("ImageProcessingAndCV\output\output.mp4",fourcc,20,(600,480))
while cap.isOpened():
    ret,frame = cap.read()
    if ret ==True:
    # frame = cv2.resize(frame,(500,333))
    # frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        # cv2.imshow("frame2",frame2)
        frame = cv2.resize(frame, (600, 480)) # important line
        output.write(frame)
        k = cv2.waitKey(25)
        if k==ord("q"):
            break
cap.release()
output.release()
cv2.destroyAllWindows()