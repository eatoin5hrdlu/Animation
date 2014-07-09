import capture
import delete
import display
import play
import save
import init
def getInput ():
	
## read buttons/keys
## if Raspberry Pi, read gpio pins
	print "get input"
	import cv2
	import sys
	import RPi.GPIO as GPIO
	from time import sleep

	print "python version " + sys.version
	print "cv version " + cv2.__version__

	stFileName = "frame"
	pin7 = 7
	x = 0

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	webcam = cv2.VideoCapture(0)

	try:
		if webcam.isOpened():
			print "Press Esc to exit"
			webcam.read() #discard first frame from webcam to make sure image is in sync 
			print "Press the button to take a picture"
			while True:
				ret, frame = webcam.read()
				cv2.imshow("window", frame)
				#if not GPIO.input(pin7):
				#	cv2.imshow("window", frame)
				#	x=x+1
				#	cv2.imwrite(stFileName+str(x)+".jpg",frame)
				#	print "Button pressed " + str(x) + " times."
				x=cv2.waitKey(10)
				if x == 27:
					break
				elif x ==	ord('n'): # Replace with the acsii value
					print "n key pressed"
					init.newMovie()
				elif x == ord(' '):
					capture.captureImage() 
					print "space key pressed"
				elif x ==	ord('d'): # Replace with the acsii value
					print "d key pressed"
					delete.deleteImage()
				elif x ==	ord('p'): # Replace with the acsii value
					print "p key pressed"
					play.playVideo()
				elif x ==	ord('-'): # Replace with the acsii value
					print "- key pressed"
					play.slower()
				elif x ==	ord('='): # Replace with the acsii value
					print "= key pressed"
					play.faster()
				elif x ==	ord('u'): # Replace with the acsii value
					print "u key pressed"
					save.uploadVideo()
						
				sleep(0.2)
		else:
			ret=False
			print "Error webcam not detected."

	finally:
		GPIO.cleanup()
		cv2.destroyAllWindows()
		print "Done."
