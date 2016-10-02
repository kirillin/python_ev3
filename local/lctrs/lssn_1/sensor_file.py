#!/usr/bin/python
from ev3dev.auto import ColorSensor, Screen, Sound, INPUT_1
from time import sleep, time


color = ColorSensor(INPUT_1)
color.mode = color.MODE_COL_REFLECT

lcd = Screen()
Sound().beep()

fout = open("data.txt", "w")
start_time = time()
for i in range(0, 100):
    t = time() - start_time
    light = color.value()
    lcd.clear()
    lcd.draw.text((0,10),"light is " + str(light))
    lcd.update()
    s = "%f\t%d\n" % (t, light)
    fout.write(s)
    sleep(0.05)
fout.close()