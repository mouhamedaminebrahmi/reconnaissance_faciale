import cv2, os, sys, time
import numpy as np
from PIL import Image
from configs import *

video_capture = cv2.VideoCapture(0) #Set the source webcam

print("Enter 'c' to capture the photo\n")
print("Enter 'q' to quit..\n\n")
print("Waiting to capture photo......\n\n")

while(video_capture.isOpened()):  # check !
    # capture frame-by-frame
    ret, frame = video_capture.read()

    if ret: # check ! (some webcam's need a "warmup")
        # our operation on frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)

	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		print("Quitting..")
		break
		
	if cv2.waitKey(1) & 0xFF == ord('c'):
		#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#name = input("Enter name: ") #For Python 3
		name = raw_input("Enter name: ") #For Python 2
		neram = str(int(time.time()))
		cv2.imwrite(db_path+"/"+str(name)+"."+neram+".png", gray)
		print("Saved as "+str(name)+"."+neram+".png"+"\n\n")
		print("Waiting to capture photo......")

print("\n\nPROCESS STOPPED......")
video_capture.release()
cv2.destroyAllWindows()