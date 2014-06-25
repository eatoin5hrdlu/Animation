import subprocess

##mplayer -mf fps=25:type=jpg *.jpg mf://*.jpg
def playVideo ():
	print "playVideo"
	stPath = "./numbers/frame"
	# Temporarily use mplayer to render and play the video
	videocmd = "mplayer -mf fps=5:type=jpg *.jpg mf://./numbers/*.jpg"
	process = subprocess.call(videocmd, shell=True)

playVideo()