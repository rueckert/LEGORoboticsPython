#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
ev3 = EV3Brick()



# Aufgabe 1: Hello World
# Erzeuge einer Konsolenausgabe(print-Befehl). Es soll "Program starting" ausgegeben werden. 
# Dieser String(Text) soll erst in einer Variable(beliebiger Name) gespeichert werden und dann ausgegeben werden.
# TODO: Aufgabe bearbeiten

# Aufgabe 2: Endlosschleife
# Schreibt eine While-Schleife die endlos lange läuft.
# In der Schleife gebt ihr die Variable counter aus und erhöht den counter jedes mal um eins.
# Nachdem es funktioniert hat, müsst ihr die While-Schleife mit '#' auskommentieren, 
# weil sonst der Rest von dem Script nicht ausgeführt wird.
counter = 0
# TODO: Aufgabe bearbeiten



# Aufgabe 3: While-Schleife
# Jetzt soll ein Countdown von 10 ausgegeben werden. 
# Dafür sollt ihr eine While-Schleife benutzen und die Variable count ausgeben,
# die mit 10 initialisiert wird und in jeder Iteration der Schleife verringert werden soll.
# Baut auch eine Pause in jeder Iteration mit dem wait-Befehl ein. 
# Später könnt ihr diese Wartezeit auskommentieren(mit '#') damit ihr nicht bei jedem Test warten müsst.
count = 10
# TODO: Aufgabe bearbeiten



# Aufgabe 4: EV3 Button
# Das Programm soll erst gestartet werden wenn der mittlere Button auf dem EV3 gedrückt wird. 
# Dafür sollt ihr eine While-Schleife und die ev3.buttons.pressed() Funktion benutzten.
# Wenn der Button gedrückt wurde soll in der Konsole "Program started" ausgegeben werden
center_pressed = Button.CENTER in ev3.buttons.pressed() # Zustand des mittleren Button(Boolean). Variable muss in Schleife aktualisiert werden
# TODO: Aufgabe bearbeiten

# Da ein Roboter in der Regel immer wieder die Sensorwerte aktualisieren und evaluieren muss 
# und die Motoren entsprechend steuern soll, ist es fast immer sinnvoll 
# eine "Dauerschleife" zu haben, die solange läuft bis das Programm beendet ist.
# Für die nächsten Aufgaben soll diese While-Schleife also nicht beendet werden.

# Um Motoren und Sensoren zu benutzen müsst ihr sie erst initialisieren. 
# Dabei müsst ihr angeben an welchen Port die Motoren/ Sensoren angeschlossen sind.
# Ändert also in den nächsten Zeilen die Ports so, dass sie zu eurem Roboter passen
# und entfernt das '#' um den Kommentar aufzuheben
# TODO: Ports anpassen:
#touchSensor = TouchSensor(Port.S1)
#ultrasonicSensor =  UltrasonicSensor(Port.S2)

#leftMotor = Motor(Port.A)
#rightMotor = Motor(Port.B)

program_running = True
#while program_running:
    # Aufgabe 4: If-Satz und Soundausgabe
    # Wenn der obere Button gedrückt ist soll ein Ton über brick.sound.beep() gespielt werden.
    # TODO: Aufgabe bearbeiten
    
    # Aufgabe 5: Motorsteuerung und Berührungssensor
    # Prüft nun ob der Berührungssensor gedrückt wurde(touchSensor.pressed()). 
    # Wenn er gedrückt wurde, soll der Roboter gerade nach vorne fahren.
    # Dafür benutzt ihr zum Beispiel leftMotor.run(200) für den linken Motor(200 ist die Geschwindigkeit).
    # Falls er nicht gedrückt wurde, soll der Roboter wieder anhalten. Dafür könnt ihr zum Beispiel leftMotor.stop()
    # benutzten. 
    # TODO: Aufgabe bearbeiten


    # Aufgabe 6: Ultraschallsensor:
    # Jetzt sollt ihr die Messwerte des Ultraschallsensor auslesen und in der Konsole ausgeben.
    # Dafür braucht ihr nur ultrasonicSensor.distance()
    # TODO: Aufgabe bearbeiten

    
    
    
    

