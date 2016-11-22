# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 00:00:17 2016

@author: MPE
"""
import time
from sense_hat import SenseHat
sense=SenseHat()

nombre = raw_input("Dime tu nombre: ")

sense.show_message('Hola,',text_colour=[100,100,100])
sense.show_message(nombre,scroll_speed=0.2, text_colour=[0,100,0])
time.sleep(1)
sense.clear()