import cv2
import numpy as np
frame = cv2.imread("resources/colorBalls.png")
# frame = cv2.resize(frame, (600, 400))
while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    u_value = np.array([23,252,249])
    l_value = np.array([17,172,189])
    # creating mask
    mask = cv2.inRange(hsv, l_value, u_value)

    # filtering
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("res", res)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
