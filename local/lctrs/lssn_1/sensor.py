#!/usr/bin/python
from ev3dev.auto import ColorSensor, Screen, Sound, INPUT_1
from time import sleep, time


color = ColorSensor(INPUT_1)
color.mode = color.MODE_COL_REFLECT

lcd = Screen()
Sound().beep()

start_time = time()
while True:
    t = time() - start_time
    light = color.value()
    lcd.clear()
    lcd.draw.text((0,10),"light is " + str(light))
    lcd.update()
    sleep(0.05)
