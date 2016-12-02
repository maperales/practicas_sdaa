# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 10:45:40 2016

@author: ManoloP
"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
camera.start_preview(fullscreen=False, window=(30,30,320,240))
for i in range(0,5):
    print 5-i
    sleep(1)
camera.capture('/home/pi/imagen.jpg')
camera.stop_preview()
camera.close()
