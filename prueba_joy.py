# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 23:24:33 2016

@author: MPE
"""
from sense_hat import SenseHat
sense=SenseHat()
XANT=4
X=4
YANT=4
Y=4
color=[200,200,0]
sense.clear()
sense.set_pixel(X,Y,color)
bucle=True
while bucle:
    events = sense.stick.get_events()
    for event in events:
        if event.direction  == "down" and event.action != "released":
            Y=Y+1
            if Y == 8:
                Y=7
        if event.direction  == "up"and event.action != "released":
            Y=Y-1
            if Y == -1:
                Y=0
        if event.direction  == "left"and event.action != "released":
            X=X-1
            if X == -1:
                X=0
        if event.direction  == "right"and event.action != "released":
            X=X+1
            if X == 8:
                X=7
        if event.direction  == "middle":
            bucle=False
            
    if X!=XANT or Y != YANT:
        sense.set_pixel(XANT,YANT,[0,0,0])
        sense.set_pixel(X,Y,color)
        XANT=X
        YANT=Y          
sense.clear()
