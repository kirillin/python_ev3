#!/usr/bin/python
from ev3dev.ev3 import LargeMotor, Sound, OUTPUT_A
from time import sleep, time
from math import sin, pi

N = 1000
file_name = "data_sin.txt"

motor = LargeMotor(OUTPUT_A)
Sound().beep("-f 440 -l 100")
fout = open(file_name, "w")
sleep(0.05)
motor.reset()
start_time = time()
for i in range(0, N):
    t = (time() - start_time) * 1000
    u_float = 100 * sin(4 * pi * t / N)
    rotation = motor.position
    motor.run_direct(duty_cycle_sp=u_float)
    s = "%f\t%d\n" % (t, rotation)
    fout.write(s)
    sleep(0.001)
fout.close()
