#!/usr/bin/env python
from ev3dev.ev3 import LargeMotor, \
    OUTPUT_A, Sound, Screen
from time import time, sleep

N = 3000
file_name = "data_gyro.txt"

pwr = 100

motor = LargeMotor(OUTPUT_A)
lcd = Screen()
Sound().beep()
fout = open(file_name, "w")
sleep(0.05)
rotation = motor.position
motor.run_direct(duty_cycle_sp=pwr)
start_time = time()
for i in range(0, N):
    lcd.clear()
    t = time() - start_time
    if rotation < 354: pwr = 100
    if rotation >= 354 and rotation <= 366: pwr = 0
    if rotation > 366: pwr = -100
    motor.duty_cycle_sp = pwr
    rotation = motor.position
    line = "%f\t%d\n" % (t, rotation)
    fout.write(line)
    lcd.draw.text((0, 10), str(rotation))
    lcd.update()
fout.close()
