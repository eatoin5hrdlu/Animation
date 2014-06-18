## Calculate and show the fps rate

import cv2
import cv
import time
import datetime

##webcam = cv2.VideoCapture(0)
##ret, frame = webcam.read()
##ret, frame = webcam.read()
fps = 25
stFileName = "./numbers/frame"
##stFileName = "/home/pi/numbers/frame"

print "Displaying " + str(fps) + " fps."
cv.NamedWindow("window", flags=cv2.cv.CV_WINDOW_NORMAL)
cv.ResizeWindow("window", 640, 480)
time.sleep(1)
#while not cv2.waitKey() == 27:
#	time.sleep(.1)

##cv2.imshow("window", frame)

print "Start: " + str(datetime.datetime.now())
for x in range (1, fps+1):
	#print stFileName+str(x)+".jpg"
	frame = cv2.imread(stFileName+str(x).zfill(3)+".jpg")
	cv2.imshow("window",frame)
	if cv2.waitKey(1) == 27:
		break
	#time.sleep(1/fps)
	##time.sleep(1)

print "End: " + str(datetime.datetime.now())
time.sleep(2)
cv2.destroyAllWindows()
print "Done."