import cv2
import cv
import sys
import RPi.GPIO as GPIO
from time import sleep

print "python version " + sys.version
print "cv version " + cv2.__version__
#print opencv version
stFileName = "./frames/frame"
pin7 = 7
x = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
webcam = cv2.VideoCapture(0)

try:
	if webcam.isOpened():
		print "Press Esc to exit"
		webcam.read() #discard first frame from webcam to make sure image is in sync 
		cv.NamedWindow("window", flags=cv2.cv.CV_WINDOW_NORMAL)
		cv.ResizeWindow("window", 640, 480)
		print "Press the button to take a picture"
		while True:
			if cv2.waitKey(10) == 27:
				break
			ret, frame = webcam.read()
			cv2.imshow("window", frame)
			if not GPIO.input(pin7):
				x=x+1
				cv2.imwrite(stFileName+str(x)+".jpg",frame)
				print "Button pressed " + str(x) + " times."
			##sleep(0.2)
	else:
		ret=False
		print "Error webcam not detected."

finally:
	GPIO.cleanup()
	cv2.destroyAllWindows()
	print "Done."