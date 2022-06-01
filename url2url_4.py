#!/usr/bin/python3
#python3.10
# version 0.1 Beta
# 20220601 h12.29
# by Antonio "Visi@n" Broi

#python3 url2url_4.py -1 "url1" -2 "url2" EXAMPLE: python3 url2url_4.py -1 "url1" -2 "url2"
#https://www.lab4int.org/wp-content/uploads/2018/07/Antonio-Broi.jpg
#https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTszRrFDgTWzfgOodfbA530XE5VueU_E530IA&usqp=CAU
#data:image/jpeg;base64,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
#data:image/jpeg;base64,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


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
ap.add_argument("-p", "--shape_predictor", default="/usr/local/lib/python3.10/dist-packages/face_recognition_models/models/shape_predictor_68_face_landmarks.dat",
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
	
	
	command = ('feh '+(args["output_directory"])+'/url1'+str(filename)+'.png')
	subprocess.Popen(command, shell=True)
	
	#sistemi Apple Mac 
	#command = ('eog '+(args["output_directory"])+'/url1'+str(filename)+'.png')
	#subprocess.Popen(command, shell=True)
	
	#sistemi Windows 
	#command = ('open '+(args["output_directory"])+'/url1'+str(filename)+'.png')
	#subprocess.Popen(command, shell=True)
	
	command = ('feh '+(args["output_directory"])+'/url2'+str(filename)+'.png')
	subprocess.Popen(command, shell=True)
	
	command = ('tree')
	subprocess.Popen(command, shell=True)
	
	command = ('cat '+(args["result_comparison"])+'/'+filename+'.csv')
	subprocess.Popen(command, shell=True)
	
	#sistemi windows
	#command = ('type '+(args["result_comparison"])+'/'+filename+'.csv')
	#subprocess.Popen(command, shell=True)
	
	
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
