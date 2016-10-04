#!/usr/bin/env python
from ev3dev.auto import *
import ev3dev.ev3 as ev3
from time import sleep, time

N = 1000
file_name = "data.txt"

motor = ev3.LargeMotor(ev3.OUTPUT_A)
Sound().beep()
fout = open(file_name, "w")
sleep(0.05);
motor.reset()
motor.run_direct(duty_cycle_sp=100)
start_time = time()
for i in range(0, N):
    t = time() - start_time
    angle = motor.position
    line = '%f\t%d\n' % (t, angle)
    fout.write(line);
    sleep(0.0005)
fout.close()
