import subprocess

##mplayer -mf fps=25:type=jpg *.jpg mf://*.jpg
def playVideo ():
	print "playVideo"
	# Temporarily use mplayer to render and play the video
	videocmd = "mplayer -mf fps=25:type=jpg *.jpg mf://./frames/*.jpg"
	process = subprocess.call(videocmd, shell=True)