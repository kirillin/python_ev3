#!/usr/bin/python
from ev3dev.ev3 import Screen
from time import sleep

lcd = Screen()
lcd.clear()
lcd.draw.text((0, 10), "Hello, world!")
lcd.update()
sleep(5)