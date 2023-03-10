import cv2
import numpy as np

#Read File
new_capture = cv2.VideoCapture('test.mp4')

#check if the file opened
if (new_capture.isOpened()==False):
    print("Error opening file")

#read the video to complete
while(new_capture.isOpened()):
    ret , frame = new_capture.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

#Release wehen everything is complete
new_capture.release()
cv2.destroyAllWindows() #close all frames