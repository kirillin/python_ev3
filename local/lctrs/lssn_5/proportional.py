#!/usr/bin/env python
from ev3dev.ev3 import LargeMotor, \
    OUTPUT_A, Sound, PowerSupply
from time import time, sleep
from math import pi, copysign

N = 1000
file_name = "data_pc.txt"

Kp = 20
pwr = 0

motor = LargeMotor(OUTPUT_A)
battary = PowerSupply()
Sound().beep()
fout = open(file_name, "w")
sleep(0.05)
motor.reset()
print(motor.position)
start_time = time()
for i in range(0, N):
    t = time() - start_time
    rotation = motor.position
    e = (360 - rotation) * pi / 180
    pwr = Kp * e
    pwr = pwr / battary.measured_volts * 100
    if abs(pwr) > 100:
        pwr = copysign(1, pwr) * 100
    motor.run_direct(duty_cycle_sp=pwr)
    line = "%f\t%d\n" % (t, rotation)
    fout.write(line)
fout.close()
