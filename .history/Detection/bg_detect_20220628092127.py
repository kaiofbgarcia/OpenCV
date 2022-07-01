import numpy as np
import cv2

capture = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = capture.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    if cv2.waitKey(5) == 27 : #27 é o ESC
        break
capture.release()
cv2.destroyAllWindows()