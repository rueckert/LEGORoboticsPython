# LEGORoboticsPython
Python für Lego Mindstorm EV3

## Inhalt
* [Installation und Dokumentation](#Installation%20und%20Dokumentation)
* [Voraussetzung](#Voraussetzung)
* [Verbindung herstellen](#Verbindung%20herstellen)
  * [USB](#USB)
  * [WLAN](#WLAN)



## Installation und Dokumentation
[Offizielle Anleitung](https://le-www-live-s.legocdn.com/sc/media/files/ev3-micropython/getting%20started%20with%20micropython_de-3619c654757bdefde79e650951c58d8a.pdf)

[Einführungspräsentation](https://docs.google.com/presentation/d/1aI6rTUCZh44TUXAJdzgp6wt7Sxh3pLjRxMZmbWnKNWI/edit?usp=sharing)

## Voraussetzung
* Visual Studio Code mit der Erweiterung [LEGO® MINDSTORMS® EV3 MicroPython](https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython)
* Einen EV3 mit einer microSD-Karte worauf das [Micropython Image](https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3) installiert ist

## Verbindung herstellen
Durch die EV3 MicroPython Erweiterung kann man mit dem EV3DEV Device Browser in Visual Studio Code eine Verbindung mit derm EV3 herstellen.

<img src="Anleitungen/assets/ConnectGuide1.png" width="300">

### USB
Wenn der EV3 über USB verbunden ist, sollte er automatisch erkannt werden.

<img src="Anleitungen/assets/ConnectGuide2.png" width="400">

### WLAN
Um den EV3 über WLAN zu verbinden muss der PC und der EV3 im gleichen Netzwerk sein. Auf dem EV3 kann man sich einfach über das Interface verbinden:

<img src="Anleitungen/assets/WLANGuide1.png" width="150"><img src="Anleitungen/assets/WLANGuide2.png" width="150"><img src="Anleitungen/assets/WLANGuide3.png" width="150"><img src="Anleitungen/assets/WLANGuide4.png" width="150"><img src="Anleitungen/assets/WLANGuide7.png" width="150">

Falls der EV3 weiterhin nicht automatisch erkannt wird, gehe in Visual Studio Code auf `I don't see my device` und gebe anschließend einen Namen für die Verbindung und die IP-Adresse des EV3 an. 

<img src="Anleitungen/assets/WLANGuide6.png" width="400">

Die IP-Adresse wird in der oberen linken Ecke des Menüs angezeigt.

<img src="Anleitungen/assets/WLANGuide8.png" width="150">

## Neues Projekt erstellen
Ein neues Projekt kann man erstellen, indem man auf die EV3 Erweiterung klickt und `Create a new project` auswählt.

<img src="Anleitungen/assets/NewProject.png" width="400">
In dem neu erstellten Project wird automatisch eine main.py Datei angelegt die alle wichtigen Klassen importiert und einen Piepton spielt. Wenn man sich also später keine Gedanken darüber machen möchte, welche Klassen man importiert kann man in jeder Klasse einfach wie in der main.py alles wichtige importieren:

`from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase`

In der ersten Zeile von jedem Python-Skript muss angegeben werden, welche Version von Python benutzt wird. In diesem Fall ist das also: 

`#!/usr/bin/env pybricks-micropython`



