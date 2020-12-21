#!/usr/bin/python3

# by Antonio "Visi@n" Broi

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
import argparse
import dlib
from imutils import face_utils
import hashlib
import requests

import optparse

#-*- coding: utf-8 -*-

def md5Checksum(filePath,url):
    if url==None:
        with open(filePath, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()
    else:
        r = requests.get(url, stream=True)
        m = hashlib.md5()
        for line in r.iter_lines():
            m.update(line)
        return m.hexdigest()

	
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape_predictor", default="/usr/local/lib/python2.7/dist-packages/face_recognition_models/models/shape_predictor_68_face_landmarks.dat",
	help="path to facial landmark predictor")
ap.add_argument("-1", "--url1", default="https://pyxis.nymag.com/v1/imgs/c71/fb1/c5e5566dc3a6fe3db549e6042becb92415-04-charlize-theron.rsquare.w330.jpg", #required = True,
	help="THE FIRST URL IMAGE")
ap.add_argument("-2", "--url2", default="https://4.bp.blogspot.com/-CbRqTz_mINY/T8SkVwME65I/AAAAAAAATqU/A1o6qgabPF4/s1600/Charlize+Theron.jpg", #required = True,
	help="THE FIRST URL IMAGE")
ap.add_argument("-o", "--output_directory", default="output",# required=True,
	help="path to original images")
ap.add_argument("-s", "--save_images", default="images",# required=True,
	help="path to output images with key points face locations")
ap.add_argument("-r", "--result_comparison", default="result",# required=True,
	help="path to output the results of comparison in csv txt format")
		

args = vars(ap.parse_args())

if not os.path.exists((args["save_images"])):
	os.makedirs((args["save_images"]))
if not os.path.exists((args["output_directory"])):
	os.makedirs((args["output_directory"]))
if not os.path.exists((args["result_comparison"])):
	os.makedirs((args["result_comparison"]))


print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

###################################################
def draw_border(frame, pt1, pt2, color, thickness, r, d):
    x1,y1 = pt1
    x2,y2 = pt2

    # Top left
    cv2.line(frame, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(frame, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(frame, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(frame, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(frame, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(frame, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(frame, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(frame, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(frame, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(frame, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(frame, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(frame, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)



###################################################
# Initialize some variables
face_locations = []
face_encodings = []
face_locations2 = []
face_encodings2 = []
face_names = []
process_this_frame = True

###############################
global url1
global url2
#url1='https://pyxis.nymag.com/v1/imgs/c71/fb1/c5e5566dc3a6fe3db549e6042becb92415-04-charlize-theron.rsquare.w330.jpg'
#url2='https://4.bp.blogspot.com/-CbRqTz_mINY/T8SkVwME65I/AAAAAAAATqU/A1o6qgabPF4/s1600/Charlize+Theron.jpg'

url1 = str(args["url1"])
url2 = str(args["url2"])

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

#############
face_locations = face_recognition.face_locations(small_frame)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 0)

for rect in rects:
		
	shape = predictor(gray, rect)
	shape = face_utils.shape_to_np(shape)

	for (x, y) in shape:
		cv2.circle(frame, (x, y), 1, (0, 0, 255), 3)

for top, right, bottom, left in face_locations:
       
	top *= 4
	right *= 4
	bottom *= 4
	left *= 4

       
	face_image = frame[top:bottom, left:right]
	draw_border(frame, (left, top), (right, bottom), (0, 0, 255), 3, 10, 20)

#############

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

#############
face_locations2 = face_recognition.face_locations(small_frame2)
gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
rects2 = detector(gray2, 0)

for rect in rects2:
		
	shape = predictor(gray2, rect)
	shape = face_utils.shape_to_np(shape)

	for (x, y) in shape:
		cv2.circle(frame2, (x, y), 1, (0, 0, 255), 3)

for top, right, bottom, left in face_locations2:
       
	top *= 4
	right *= 4
	bottom *= 4
	left *= 4

       
	face_image2 = frame2[top:bottom, left:right]
	draw_border(frame2, (left, top), (right, bottom), (0, 0, 255), 3, 10, 20)

#############


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
	intero_face_dist_perc = int(face_distance_percent) 
	print('Result comparation of :')
	print('URL 1 : '+str(url1))
	print('URL 2 : '+(url2))
	print('########################################')
	print('RESULT : '+str(matches))
	print('PERCENTAGE OF COMPARISON : '+str(intero_face_dist_perc)+'% \n')
		
	# Display the resulting image
	#cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
	filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
	
	if not os.path.isdir(args["output_directory"]): os.mkdir(args["output_directory"])
	cv2.imwrite((args["output_directory"])+'/url1'+str(filename)+'.png', frame)
	cv2.imwrite((args["output_directory"])+'/url2'+str(filename)+'.png', frame2)
	
	cv2.imwrite((args["save_images"])+'/url1'+str(filename)+'.png', frame)
	cv2.imwrite((args["save_images"])+'/url2'+str(filename)+'.png', frame2)
	
	##md5Checksum(filePath,url) #HASH URL
	#md5url1 = md5Checksum(None,url1)
	#md5url2 = md5Checksum(None,str(url2))
	
	#md5url1 = hashlib.md5(url1)
	#md5url2 = hashlib.md5(url2)
	
	##md5Checksum(filePath,url) #HASH FILE IMAGES
	#md5file1 = md5Checksum((args["save_images"])+'/url1'+str(filename)+'.png',None)
	#md5file2 = md5Checksum((args["save_images"])+'/url2'+str(filename)+'.png',None)
	
	
	file1 = ((args["save_images"])+'/url1'+str(filename)+'.png')#,"r", encoding='utf-8')
	openFile1 = open(file1, "rb")
	readFile1 = openFile1.read()
	
	md5hash1 = hashlib.md5(readFile1)
	md5file1 = md5hash1.hexdigest()
	
	sha1hash1 = hashlib.sha1(readFile1)
	shafile1 = sha1hash1.hexdigest()
	
	openFile1.close()
	
	file2 = ((args["save_images"])+'/url2'+str(filename)+'.png')#,"r", encoding='utf-8')
	openFile2 = open(file2, "rb")
	readFile2 = openFile2.read()
	
	md5hash2 = hashlib.md5(readFile2)
	md5file2 = md5hash2.hexdigest()
	
	sha1hash2 = hashlib.sha1(readFile2)
	shafile2 = sha1hash2.hexdigest()
	
	openFile2.close()
	
	
	
	file = open((args["result_comparison"])+'/'+filename+'.csv', 'w+')
	file.write('COMPARIZON BETWEEN : \n'+str(url1)+' \n md5 url 1 : \n'+str(md5file1)+'\n sha url 1 : \n'+str(shafile1)+'\n'+str(url2)+' \n md5 url 2 : \n'+str(md5file1)+'\n sha url 2 : \n'+str(shafile2)+'\n'+str(matches)+' \n '+str(intero_face_dist_perc)+'% \n'+'eseguita al time-stamp : '+str(filename))
	file.close()
	
	
	command = ('eog '+(args["output_directory"])+'/url1'+str(filename)+'.png')
	subprocess.Popen(command, shell=True)
	
	command = ('eog '+(args["output_directory"])+'/url2'+str(filename)+'.png')
	subprocess.Popen(command, shell=True)
	
	command = ('tree')
	subprocess.Popen(command, shell=True)
	
	command = ('cat '+(args["result_comparison"])+'/'+filename+'.csv')
	subprocess.Popen(command, shell=True)
	
	
	cv2.imshow('url1', frame)
	# Hit 'q' on the keyboard to quit!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		exit
	
	cv2.imshow('url2', frame2)
	# Hit 'q' on the keyboard to quit!
	if cv2.waitKey(1) & 0xFF == ord('q'):
		exit

		

# Release handle to the webcam
##video_capture.release()
cv2.destroyAllWindows()
