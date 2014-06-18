import cv2
import sys

print "python version " + sys.version
print "cv version " + cv2.__version__
#print opencv version
stFileName = "out.jpg"
  
webcam = cv2.VideoCapture(0)

if webcam.isOpened():
	print "Press Esc to exit"
	webcam.read() #discard first frame from webcam to make sure image is in sync 
	ret, frame = webcam.read()
	blur = cv2.GaussianBlur(frame,(0,0),5)
	cv2.imshow("window", frame)
#	cv2.imwrite(stFileName,frame)
#	imgFile = cv2.imread(stFileName)
#	cv2.imshow("window",imgFile)
else:
	ret=False
	print "Error webcam not detected."
while True:
        if cv2.waitKey(10) == 27:
                cv2.destroyAllWindows()
                break
print "done"
	

