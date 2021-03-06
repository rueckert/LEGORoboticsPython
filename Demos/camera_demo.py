#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import (Port, Button)
from pybricks.tools import print, wait
from pybricks.ev3devices import ColorSensor
import time
import math


#Fuege den Tools Ordner zum PYTHONPATH hinzu. Nicht notwendig wenn TOF.py im selben Ordner ist
import sys
sys.path.append("/home/robot/LEGORoboticsPython/Tools")
from pixy_camera import *

ev3=EV3Brick()
#Port des Sensors festlegen
camera = Camera(Port.S1)
#c = ColorSensor(Port.S3)
camera.lamp_on()

while not Button.DOWN in ev3.buttons.pressed():
    #x2,y2,w2,h2=camera.getObjectData(2,False)
    #x1,y1,w1,h1=camera.getObjectData(1,True)


    #result =  'Camera x1: ' + str(x1)
    #print(result)
    angle,data = camera.get_line_tracking_angle()
    print(angle)
    #print(data.number_of_barcodes)
    for b in data.barcodes:
        print("Code: "+str(b.code)+' Flag: '+str(b.flags))

    
    data.clear()
    wait(20)
camera.lamp_off()
camera.close()
