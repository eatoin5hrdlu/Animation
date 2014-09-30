from Tkinter import *
from ttk import *
import const
import cv2
import sys
import os
import errno
import glob
import subprocess
import time
import numpy as np


def deleteImage ():
	global framenum
	global lastFrame

	print "deleteImage"
	if framenum > 0:
		stFileName = FILE_PATH + str(framenum).zfill(FILENAME_LENGTH)+".jpg"
		os.unlink(stFileName)
		print "Deleted " + stFileName
		framenum = framenum - 1
		## Load the previous frame into lastFrame so the onionskin effect works
		if framenum > 0:
			lastFrame = cv2.imread(FILE_PATH + str(framenum).zfill(FILENAME_LENGTH)+".jpg")
		else:
			lastFrame = ""
		modifiedMovie()


def displayImage ():
	print "displayImage"
	framenum = framenum + 1
	print "framenum=" + str(framenum)


def initializeCamera ():
	print "initializing camera"
	global webcam
	
	webcam = cv2.VideoCapture(CAMERA)
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
	answer = ""
	print "newMovie called"
	if framenum > 20 and modified == True:
		answer = raw_input( "Do you want to save your changes (y/n)?" ) ####use raw_input instead of input####
		if answer == 'y' :
			saveVideo()
			# should we reset the program here, or press new movie again?
		else:
			resetProgram()
	else:
		resetProgram()		
		

def resetProgram():
	global fps
	global lastFrame
	global framenum
	print "Clearing the frames directory"
	pathStr = FILE_PATH + "*.jpg"
	for filename in glob.glob(pathStr):
		os.remove( filename )
	# clear filmstrip on screen
	# reset frame rate variable
	fps = const.DEFAULT_FPS
	# clear last frame
	lastFrame=""
	framenum=0
	# reset framenum


def resumeProgram():
	global framenum
	global lastFrame
	#global avg1
	
	print "resumeProgram"
	pathStr = FILE_PATH + "*.jpg"
	files  = glob.glob(pathStr)
	files.sort()
	for filename in files:
		print filename
	#if frames exist
	framenum = len(files)
	
	if framenum > 0:
		#display last image
		stFileName = FILE_PATH + str(framenum).zfill(FILENAME_LENGTH)+".jpg"
		lastFrame = cv2.imread(FILE_PATH + str(framenum).zfill(6)+".jpg")
		#avg1 = np.float32(lastFrame)
	#initialize filmstrip display
	
def modifiedMovie():
	print "modifiedMovie called"
	global modified
	global savedMovies
	
	modified = True
	savedMovies = "" # Clear the history of saved movies
	

def captureImage ():
	global framenum
	global webcam
	global lastFrame
	#global avg1
	print "captureImage"
	
	ret, lastFrame = webcam.read()
	#avg1=np.float32(lastFrame)
	framenum = framenum + 1 
	stFileName = FILE_PATH + str(framenum).zfill(FILENAME_LENGTH)+".jpg" 
	cv2.imwrite(stFileName,lastFrame)
	print "Saved " + stFileName
	modifiedMovie()	



def playVideo ():
	print "playVideo"
	# Temporarily use mplayer to render and play the video
	# decide whether to show images and delay or render the video
	global fps	# Should this be global?
	frames=[]
	print "frames=" + str(framenum)
	#videocmd = "mplayer -mf fps=" + str(fps) + ":type=jpg *.jpg mf://" + FILE_PATH + "*.jpg"
	#process = subprocess.Popen(videocmd, shell=True)
	for x in range (1, framenum+1):
		frame = cv2.imread(FILE_PATH + str(x).zfill(6)+".jpg")
		frames.append(frame)

	cv2.imshow("play window",frames[0])
	cv2.waitKey(500)

	for x in range (0, framenum):
		cv2.imshow("play window",frames[x])
		keycode = cv2.waitKey(1)
		time.sleep(1/fps)
	#wait 1 second before closing the window
	time.sleep(1)
	cv2.destroyWindow("play window")

	
def saveVideo():
	print "playVideo"
	# Temporarily use mplayer to render and play the video
	global fps
	FPS_OUT=24
	if framenum > 0:
		videocmd = "mplayer -mf fps=" + str(fps) + ":type=jpg *.jpg mf://" + FILE_PATH + "*.jpg"
		#process = subprocess.Popen(videocmd, shell=True)
		#avconv -i ./*.jpg -r 3 movie.mp4	
		#avconv -f image2 -i frame%03d.jpg -r 12 -s 160x120 movie.avi
		#os.system("avconv -r %s -i frame%03d.jpg -r %s -vcodec libx264 -crf -g 15 movie.mp4"%(fps,FPS_OUT))
		#videocmd="avconv -r " + str(fps) + " -i ./frames/%06d.jpg -r " + str("24") + "-vcodec libx264 -crf -g 15 movie.mp4"
		videocmd="avconv -r " + str(fps) + " -i " + FILE_PATH + "%06d.jpg -r " + str("24") + " " + MOVIE_PATH + "movie.mpg" # generate movie filename
		print "videocmd = " + videocmd
		# process = subprocess.Popen(videocmd, shell=True) # works, but trying with call instead
		process = subprocess.call(videocmd, shell=True)
		#os.system(videocmd)
		print "finished saving"
	

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
	

def uploadVideo():
	print "uploadVideo"
	if framenum > 0:
		print "upload"


def getInput ():
## read buttons/keys
	print "get input"
	keycode = 0
	global webcam
	global lastFrame
	#global avg1
	
	avgTemp=[]
	while True:
		ret, frame = webcam.read()
#		if framenum > 0:
#			avg1 = np.float32(lastFrame)
#			#np.copyto(avgTemp,avg1)
#			#avgTemp = np.array(avg1)
#			cv2.accumulateWeighted(frame, avg1, ALPHA) #ALPHA was 0.5 for this method
#			frame = cv2.convertScaleAbs(avg1)
#		cv2.imshow("Live Video", frame)
		if framenum > 0:
			# Try using Python Imaging Library for the onionskin effect
			frame = cv2.addWeighted(frame, 1, lastFrame, ALPHA, 0)  #ALPHA is 0.2

		cv2.imshow("Live Video", frame)

		keycode = cv2.waitKey(10)
		if keycode > 255:
			print "Make sure caps lock and num lock are off!  Keycode=" + str(keycode)
		if keycode == 27:
			break
		elif keycode == ord(NEWMOVIEKEY): # Replace with the acsii value
			print "n key pressed"
			newMovie()
		elif keycode == ord(CAPTUREIMAGEKEY):
			captureImage() 
			print "space key pressed"
		elif keycode ==	ord(DELETEIMAGEKEY): # Replace with the acsii value
			print "d key pressed"
			deleteImage()
		elif keycode ==	ord(PLAYVIDEOKEY): # Replace with the acsii value
			print "p key pressed"
			playVideo()
		elif keycode ==	ord(SLOWERKEY): # Replace with the acsii value
			print "- key pressed"
			slower()
		elif keycode ==	ord(FASTERKEY): # Replace with the acsii value
			print "= key pressed"
			faster()
		elif keycode ==	ord(UPLOADVIDEOKEY): # Replace with the acsii value
			print "u key pressed"
			uploadVideo()
		elif keycode ==	ord(SAVEVIDEOKEY): # Replace with the acsii value
			print "s key pressed"
			saveVideo()
						
		time.sleep(0.05)

def pathExists(path):
	try:
		os.makedirs(path)
	except OSError as exception:
		if exception.errno !=errno.EEXIST:
			raise

def setupGui():
	root = Tk()
	root.title ('Animation Station')
	root.overrideredirect(True)  # no window decorations
	root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
	
	mainframe = Frame(root, padding = '3 3 12 12')
	mainframe.grid(column=0, row = 0, sticky=(N,W,E,S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0,weight=1)
	
	root.mainloop()

### Golbal Variables ###
root = ""
mainframe = ""
### Initialize variables ###
fps = const.DEFAULT_FPS
MAX_FPS = const.MAX_FPS
MIN_FPS = const.MIN_FPS
FPS_STEP = const.FPS_STEP
FILENAME_LENGTH = const.FILENAME_LENGTH
FILE_PATH = const.FILE_PATH
MOVIE_PATH = const.MOVIE_PATH
ALPHA = const.ALPHA
CAMERA=const.CAMERA
NEWMOVIEKEY = const.NEWMOVIEKEY
CAPTUREIMAGEKEY = const.CAPTUREIMAGEKEY
DELETEIMAGEKEY = const.DELETEIMAGEKEY
PLAYVIDEOKEY = const.PLAYVIDEOKEY
SLOWERKEY = const.SLOWERKEY
FASTERKEY = const.FASTERKEY
UPLOADVIDEOKEY = const.UPLOADVIDEOKEY
SAVEVIDEOKEY = const.SAVEVIDEOKEY
framenum=0
lastFrame=""
webcam=""
avg1=[]
avgbackup=[]
modified = True	# Track unsaved changes
savedMovies = "" # Track saved versions when modified = False, clear when modified = True
#avg1=np.float32(1)
#create frames and movie directories if they don't exist
pathExists(FILE_PATH)
pathExists(MOVIE_PATH)

### Main program ###
try:
	printVersions()
	if initializeCamera() == True:
		resumeProgram()
		# SetupGui()
		getInput()
finally:
	cv2.destroyAllWindows()
	webcam.release()
	print "Done."
