from SimpleCV import Camera, Display
from time import sleep
myCamera = Camera(prop_set={'width': 320, 'height': 240})
frame = myCamera.getImage()
frame.save("camera-output.jpg")
print "Done."
