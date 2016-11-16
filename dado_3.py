from sense_hat import SenseHat
from time import sleep
from random import randint

sense=SenseHat()
#sense.set_rotation(180)
#X= [255, 0, 0]  # Red
#O = [255, 255, 255]  # White
A=[0,0,0]
NADA=[
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
A,A,A,A,A,A,A,A,
]

numeros=[NADA,NADA,NADA,NADA,NADA,NADA]

def define_nums(fondo,punto):
  global numeros
  O=fondo
  X=punto
  UNO = [
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  ]
  
  DOS = [
  X, X, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, X, X,
  O, O, O, O, O, O, X, X,
  ]
  
  TRES = [
  X, X, O, O, O, O, O, O,
  X, X, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, X, X,
  O, O, O, O, O, O, X, X,
  ]
  
  CUATRO = [
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  ]
  
  CINCO = [
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  O, O, O, O, O, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, O, O, O, O, O,
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  ]
  
  SEIS = [
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  O, O, O, O, O, O, O, O,
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  O, O, O, O, O, O, O, O,
  X, X, O, O, O, O, X, X,
  X, X, O, O, O, O, X, X,
  ]
  numeros=[UNO, DOS, TRES, CUATRO, CINCO, SEIS]

define_nums([255,0,0],[255,255,0])
Ciclo=True
corre=True
while Ciclo:
  if corre:
       num=randint(0,5)
       sense.set_pixels(numeros[num])
       events = sense.stick.get_events()
       for event in events:
           if event.direction  == "down":
               corre=False
  else :
      define_nums([0,255,0],[255,0,0])
      sense.set_pixels(numeros[num])
      events = sense.stick.get_events()
      for event in events:
           if event.direction   == "up":
               define_nums([255,0,0],[255,255,0])
               corre=True
           if event.direction == 'right':
               Ciclo= False

sense.clear()

            
    
