# https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
  
from cv2 import *
  
cam_port = 0
cam = VideoCapture(cam_port)
result, image = cam.read()
  
if result:  
    imwrite("GeeksForGeeks.png", image)
  
else:
    print("Error!")
