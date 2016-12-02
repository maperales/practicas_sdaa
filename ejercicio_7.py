# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 14:38:19 2016

@author: ManoloP
"""
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.rotation = 180
camera.hflip = True
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array         
    cv2.imshow("Previsualizacion", image)  
    key = cv2.waitKey(1) & 0xFF  
    rawCapture.truncate(0)
    if key == ord("q"):
         cv2.imwrite("foto_7.jpg",image)
         break
camera.close()  
cv2.destroyWindow("Previsualizacion") 




