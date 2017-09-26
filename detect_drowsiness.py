from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
import imageio
#import visvis as vv

from gi.repository import Gdk
#from SimpleCV import Camera
import sys

def sound_alarm(path):
	playsound.playsound(path)

def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)
	return ear


def main():
	args = {}
	args["shape_predictor"] = "/home/rock19/Desktop/drowsiness-detection/shape_predictor_68_face_landmarks.dat"
	args["alarm"] = "/home/rock19/Desktop/drowsiness-detection/alarm.wav"
	 
	EYE_AR_THRESH = 0.26
	EYE_AR_CONSEC_FRAMES = 20
	
	earpre=np.zeros(2)
	ear=np.zeros(2)
	count=np.zeros(2)
	
	COUNTER = 0
	ALARM_ON = False

	print("[INFO] loading facial landmark predictor...")
	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor(args["shape_predictor"])

	# grab the indexes of the facial landmarks for the left and
	# right eye, respectively
	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

	# start the video stream thread
	print("[INFO] starting video stream thread...")


	#vs = cv2.VideoCapture('<video0>') #26582
	#cv2.namedWindow("Window")
	#if (vs.isOpened() == False): 
	#  print("Error opening video stream or file")
	  
	reader = imageio.get_reader('<video0>')
	#t = vv.imshow(reader.get_next_data(), clim=(0, 255))

	time.sleep(1.0)  # If you don't wait, the image will be dark

	i=1
	# loop over frames from the video stream
	TEAM=True

	while TEAM:

		#var, frame = vs.read()
		#frame = cv2.imread('/home/rock19/Desktop/new/Pictures%d.jpg' % i)
			
		for frame in reader:

			if not TEAM:
				break
			#vv.processEvents()
			#t.SetData(frame)

			frame = imutils.resize(frame, width=450)
			gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
			
			# detect faces in the grayscale frame
			rects = detector(gray, 0)

			# loop over the face detections
			j=0
			for rect in rects:

				if j>1:
					print 'More persons than expected!!!!'
					continue

				# determine the facial landmarks for the face region, then
				# convert the facial landmark (x, y)-coordinates to a NumPy
				# array
				shape = predictor(gray, rect)
				shape = face_utils.shape_to_np(shape)

				# extract the left and right eye coordinates, then use the
				# coordinates to compute the eye aspect ratio for both eyes
				leftEye = shape[lStart:lEnd]
				rightEye = shape[rStart:rEnd]
				leftEAR = eye_aspect_ratio(leftEye)
				rightEAR = eye_aspect_ratio(rightEye)

				# average the eye aspect ratio together for both eyes
				ear[j] = (leftEAR + rightEAR) / 2.0

				# compute the convex hull for the left and right eye, then
				# visualize each of the eyes
				leftEyeHull = cv2.convexHull(leftEye)
				rightEyeHull = cv2.convexHull(rightEye)
				cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
				cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

				# check to see if the eye aspect ratio is below the blink
				# threshold, and if so, increment the blink frame counter

				if j<2:
					if earpre[j] - ear[j] > 0.05:
						count[j] += 1
						
						if count[j] > 5:
							print 'Player ',j+1,' loses\n'
							print 'Score: ',abs(count[j]-count[j^1]),'\n'
							cv2.destroyAllWindows()
							TEAM=False
							break
							

						print 'blink',(j+1)

				earpre[j]=ear[j]

				if ear[j] < EYE_AR_THRESH:
					COUNTER += 1

					# if the eyes were closed for a sufficient number of
					# then sound the alarm
					'''
					if COUNTER >= EYE_AR_CONSEC_FRAMES:
						# if the alarm is not on, turn it on
						if not ALARM_ON:
							ALARM_ON = True

							# sound played in the background
							if args["alarm"] != "":
								th = Thread(target=sound_alarm,
									args=(args["alarm"],))
								th.deamon = True
								th.start()

						# draw an alarm on the frame

						cv2.putText(frame, "DROWSINESS ALERT!", (200, 30),
							cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

					'''

				# otherwise, the eye aspect ratio is not below the blink
				# threshold, so reset the counter and alarm
				else:
					COUNTER = 0
					ALARM_ON = False

				# draw the computed eye aspect ratio on the frame to help
				# with debugging and setting the correct eye aspect ratio
				# thresholds and frame counters
				cv2.putText(frame, "EAR: {:.2f}".format(ear[j]), (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


				if(j==0):
					cv2.putText(frame, "{:.0f}".format(count[j]), (10, 300),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

				if(j==1):
					cv2.putText(frame, "{:.0f}".format(count[j]), (300, 300),
						cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				
				j += 1
		 
		 	if not TEAM:
		 		break
			# show the frame
			cv2.imshow("Frame", frame)
			key = cv2.waitKey(1) & 0xFF
			i += 1

		break

	# do a bit of cleanup
	cv2.destroyAllWindows()