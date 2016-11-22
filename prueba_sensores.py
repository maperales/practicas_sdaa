# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 00:00:17 2016

@author: MPE
"""
from sense_hat import SenseHat
sense=SenseHat()

Humedad=sense.get_humidity()
Temp1=sense.get_temperature_from_humidity()
Temp2=sense.get_temperature_from_pressure()
Presion=sense.get_pressure()
print("Humedad: %2.3f" %Humedad)
print("Temperaturas: %2.3f %2.3f" % (Temp1,Temp2))
print("Presión: %4.2f" %Presion)

TStr=str(round(Temp1,2))
sense.show_message("T:"+TStr)