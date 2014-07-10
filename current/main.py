import const
import cv2
import sys
import os
import subprocess
from time import sleep


def deleteImage ():
	global framenum
	print "deleteImage"
	if framenum > 0:
		stFileName = FILE_PATH + str(framenum).zfill(FILENAME_LENGTH)+".jpg"
		os.unlink(stFileName)
		print "Deleted " + stFileName
		framenum = framenum - 1
		modifiedMovie()


def displayImage ():
	print "displayImage"
	framenum = framenum + 1
	print "framenum=" + str(framenum)


def initializeCamera ():
	print "initializing camera"
	global webcam
	
	webcam = cv2.VideoCapture(0)
	if webcam.isOpened():
		print "Press Esc to exit"
		webcam.read() #discard first frame from webcam to make sure image is in sync
		ret = True
	else:
		ret = False
		print "Error webcam not detected."
	return ret


def printVersions():
	print "python version " + sys.version
	print "cv version " + cv2.__version__


def newMovie():
	print "newMovie called"
	#if framenum > 20
	#	save movie
	# Clear frames directory
	modifiedMovie()
	
	
def modifiedMovie():
	print "modifiedMovie called"
	global modified
	global savedMovies
	
	modified = True
	savedMovies = "" # Clear the history of saved movies
	

def captureImage ():
	global framenum
	global webcam
	
	print "captureImage"
	
	ret, frame = webcam.read()
	framenum = framenum + 1
	stFileName = FILE_PATH + str(framenum).zfill(FILENAME_LENGTH)+".jpg" 
	cv2.imwrite(stFileName,frame)
	print "Saved " + stFileName
	modifiedMovie()
	



def playVideo ():
	print "playVideo"
	# Temporarily use mplayer to render and play the video
	global fps
	videocmd = "mplayer -mf fps=" + str(fps) + ":type=jpg *.jpg mf://" + FILE_PATH + "*.jpg"
	process = subprocess.Popen(videocmd, shell=True)
	
	
def saveVideo ():
	print "playVideo"
	# Temporarily use mplayer to render and play the video
	global fps
	videocmd = "mplayer -mf fps=" + str(fps) + ":type=jpg *.jpg mf://" + FILE_PATH + "*.jpg"
	process = subprocess.Popen(videocmd, shell=True)	


def faster():
	print "faster called"
	#update flim strip to display fps rate
	global fps
	global MAX_FPS
	global FPS_STEP
	if not (fps >= MAX_FPS):
		fps = fps + FPS_STEP
	print "fps=" + str(fps)
	
	
def slower():
	print "slower called"
	#update flim strip to display fps rate
	global fps
	global MIN_FPS
	global FPS_STEP
	if not (fps <= MIN_FPS):
		fps = fps - FPS_STEP
	print "fps=" + str(fps)
	

def saveVideo():
	print "saveVideo"


def uploadVideo():
	print "uploadVideo"


def getInput ():
## read buttons/keys
	print "get input"
	keycode = 0
	global webcam
	
	while True:
		ret, frame = webcam.read()
		cv2.imshow("window", frame)
		keycode=cv2.waitKey(10)
		if keycode > 255:
			print "Make sure caps lock and num lock are off!  Keycode=" + str(keycode)
		if keycode == 27:
			break
		elif keycode == ord('n'): # Replace with the acsii value
			print "n key pressed"
			newMovie()
		elif keycode == ord(' '):
			captureImage() 
			print "space key pressed"
		elif keycode ==	ord('d'): # Replace with the acsii value
			print "d key pressed"
			deleteImage()
		elif keycode ==	ord('p'): # Replace with the acsii value
			print "p key pressed"
			playVideo()
		elif keycode ==	ord('-'): # Replace with the acsii value
			print "- key pressed"
			slower()
		elif keycode ==	ord('='): # Replace with the acsii value
			print "= key pressed"
			faster()
		elif keycode ==	ord('u'): # Replace with the acsii value
			print "u key pressed"
			uploadVideo()
						
		sleep(0.2)


### Initialize variables ###
fps = const.DEFAULT_FPS
MAX_FPS = const.MAX_FPS
MIN_FPS = const.MIN_FPS
FPS_STEP = const.FPS_STEP
FILENAME_LENGTH = const.FILENAME_LENGTH
FILE_PATH = const.FILE_PATH
framenum=0
webcam=""
modified = True	# Track unsaved changes
savedMovies = "" # Track saved versions when modified = False, clear when modified = True

### Main program ###
try:
	printVersions()
	if initializeCamera() == True:
		getInput()
finally:
	cv2.destroyAllWindows()
	print "Done."
