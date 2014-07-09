import const
import subprocess

##mplayer -mf fps=25:type=jpg *.jpg mf://*.jpg
def playVideo ():
	print "playVideo"
	# Temporarily use mplayer to render and play the video
	global fps
	videocmd = "mplayer -mf fps=" + str(fps) + ":type=jpg *.jpg mf://./frames/*.jpg"
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
	
fps = const.DEFAULT_FPS
MAX_FPS = const.MAX_FPS
MIN_FPS = const.MIN_FPS
FPS_STEP = const.FPS_STEP
