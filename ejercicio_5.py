# -*- coding: utf-8 -*-
"""
Created on Fri Dec 02 10:50:43 2016

@author: ManoloP
"""
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
camera.start_preview(fullscreen=False, window=(30,30,320,240))
camera.start_recording('/home/pi/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()




