MAX_FPS = 24
MIN_FPS = 3
FPS_STEP = 3
DEFAULT_FPS = 12
FILENAME_LENGTH = 6
FILE_PATH = "./frames/"
MOVIE_PATH = "./movies/"
ALPHA = 0.3
CAMERA = 0
# There is a memory leak in OpenCV ($Rev: 4557) when setting the camera resolution.
# Set the video and image dimensions the same to avoid the problem until OpenCV is updated in the Raspberry Pi repository.
VIDEO_WIDTH = 640
VIDEO_HEIGHT = 480
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480
NEWMOVIEKEY = 'n'
CAPTUREIMAGEKEY = ' '
DELETEIMAGEKEY = 'd'
PLAYVIDEOKEY = 'p'
SLOWERKEY = '-'
FASTERKEY = '='
UPLOADVIDEOKEY = 'u'
SAVEVIDEOKEY = 's'
UPLOADURL = "youtube"
