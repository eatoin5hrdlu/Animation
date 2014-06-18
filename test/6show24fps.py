################################################################
## We only get about 14fps on the Raspberry Pi with this code ##
################################################################

import cv2
import cv
import time
import datetime

##webcam = cv2.VideoCapture(0)
##ret, frame = webcam.read()
##ret, frame = webcam.read()
frames=[]
fps = 25
stFileName = "./numbers/frame"
##stFileName = "/home/pi/numbers/frame"

print "Displaying " + str(fps) + " fps."
cv.NamedWindow("window", flags=cv2.cv.CV_WINDOW_NORMAL)
cv.ResizeWindow("window", 640, 480)
#time.sleep(1)
#while not cv2.waitKey() == 27:
#	time.sleep(.1)

##cv2.imshow("window", frame)

for x in range (1, fps+1):
	#print stFileName+str(x)+".jpg"
	frame = cv2.imread(stFileName+str(x).zfill(3)+".jpg")
	frames.append(frame)

cv2.imshow("window",frames[0])
cv2.waitKey(500)

print "Start: " + str(datetime.datetime.now())
for x in range (0, fps):

	cv2.imshow("window",frames[x])
	if cv2.waitKey(1) == 27:
		break
	#time.sleep(1/fps)
	##time.sleep(1)

print "End: " + str(datetime.datetime.now())
time.sleep(2)
cv2.destroyAllWindows()
print "Done."