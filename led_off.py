#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 00:22:31 2016

@author: pi
"""

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
