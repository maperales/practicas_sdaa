# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 20:41:56 2016

@author: ManoloP
"""
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
camera.rotation = 180
camera.hflip = True
rawCapture = PiRGBArray(camera, size=(320, 240))

time.sleep(0.1)
print 'Saca la primera foto pulsando A'
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("A"):
         imagen1=image
         cv2.imshow("A",imagen1)
         time.sleep(3)
         print 'Saca la segunda foto pulsando B'
    if key == ord("B"):
         imagen2=image
         cv2.imshow("B",imagen2)
         time.sleep(3)
         print 'Para mezclarlas, pulsa M'
    if key == ord("M"):
         alfa=raw_input("mete porcentaje de mezcla")
         alfa_f=float(alfa)/100.0
         beta=1.0-alfa_f
         dst = cv2.addWeighted(imagen1,alfa_f,imagen2,beta,0)
         cv2.imshow("BLEND",dst)
         print "Mezcla al %s" %alfa        
         time.sleep(3)
         print 'Para salir, pulsa q'
    if key == ord("q"):
        break                  
camera.close()
cv2.destroyWindow("Frame")

