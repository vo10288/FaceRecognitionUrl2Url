import face_recognition
import cv2
import time
import os
import subprocess
from datetime import datetime
import os.path
import urllib
#import pygame
import numpy as np
#pygame.init()
import imutils
import os
###################################################
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

###############################
url1='https://pyxis.nymag.com/v1/imgs/c71/fb1/c5e5566dc3a6fe3db549e6042becb92415-04-charlize-theron.rsquare.w330.jpg'
url2='https://4.bp.blogspot.com/-CbRqTz_mINY/T8SkVwME65I/AAAAAAAATqU/A1o6qgabPF4/s1600/Charlize+Theron.jpg'

#global timenow

#while True:
	#timenow = time.localtime()
	#print(timenow)
	#print(timenow.tm_hour)
	#print(timenow.tm_min)


########## URL 1 #####################
imgResp=urllib.request.urlopen(url1) #python2 urllib.urlopen(url)
imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
global frame
frame=cv2.imdecode(imgNp, -1)
# Resize frame of video to 1/4 size for faster face recognition processing
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
rgb_small_frame = small_frame[:, :, ::-1]

#cv2.imshow(str(url1), small_frame)
########### URL 2 #######################
imgResp2=urllib.request.urlopen(url2) #python2 urllib.urlopen(url)
imgNp2=np.array(bytearray(imgResp2.read()),dtype=np.uint8)
global frame2
frame2=cv2.imdecode(imgNp2, -1)
# Resize frame of video to 1/4 size for faster face recognition processing
small_frame2 = cv2.resize(frame2, (0, 0), fx=0.25, fy=0.25)

# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
rgb_small_frame2 = small_frame2[:, :, ::-1]

#cv2.imshow(str(url2), small_frame2)
#########################################
# Only process every other frame of video to save time
if process_this_frame:
	# Find all the faces and face encodings in the current frame of url1
	face_locations = face_recognition.face_locations(rgb_small_frame)
	face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

	# Find all the faces and face encodings in the current frame of url2
	face_locations2 = face_recognition.face_locations(rgb_small_frame2)
	face_encodings2 = face_recognition.face_encodings(rgb_small_frame2, face_locations2)


	#face_names = []
		
		
#		for face_encoding in face_encodings:
            
	# See if the face is a match for the known face(s)
	matches = face_recognition.compare_faces(face_encodings, face_encodings2[0])
	face_distances = face_recognition.face_distance(face_encodings, face_encodings2[0])
	face_distance_percent = ((1-face_distances)*100) 
	print('Result comparation of :')
	print('URL 1 : '+str(url1))
	print('URL 2 : '+(url2))
	print('########################################')
	print('RESULT : '+str(matches))
	print('PERCENTUAL OF COMPARATION : '+str(face_distance_percent)+'%')
		
	# Display the resulting image
	#cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
	cv2.imwrite('url/1.png', frame)
	cv2.imwrite('url/2.png', frame2)
	cv2.imshow(str(url1), small_frame)
	cv2.imshow(str(url2), small_frame2)
	
		
   

    # Hit 'q' on the keyboard to quit!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		exit

# Release handle to the webcam
##video_capture.release()
cv2.destroyAllWindows()
