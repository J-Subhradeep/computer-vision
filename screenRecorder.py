import cv2 
import pyautogui as p
import numpy as np
rs = p.size()

file_name = "output\output.mp4"

fps = 30
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter(file_name,fourcc,fps,rs)


cv2.namedWindow("Live_Recording",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    # cv2.imshow("res",f)
    if cv2.waitKey(1)== ord("q"):
        break
output.release()
cv2.destroyAllWindows()