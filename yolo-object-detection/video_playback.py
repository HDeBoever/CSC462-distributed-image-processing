#Playing Video from File

import numpy as np
import cv2

cap = cv2.VideoCapture('./recombined_videos/video.avi')

print(cap.get(5)) #to display frame rate of video

while(cap.isOpened()):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grayscale

    cv2.imshow('frame',frame)
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
