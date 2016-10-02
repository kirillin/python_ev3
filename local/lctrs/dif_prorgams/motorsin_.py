#!/usr/bin/python
from ev3dev.ev3 import LargeMotor, Sound, OUTPUT_A
from time import sleep, time
from math import sin, pi

N = 1000

motor = LargeMotor(OUTPUT_A)
Sound().beep("-f 440 -l 100")
fout = open("data.txt", "w")
sleep(0.05)
start_time = time()
for i in range(0, N):
    t = (time() - start_time) * 1000 #так как время в микросекундах
    u_float = 100 * sin(pi * t / N)
    rotation = motor.position
    motor.run_forever(speed_sp = u_float * 10) #should use speed_sp insted duty_cycle_sp
    s = "%f\t%d\n" % (t, rotation)
    fout.write(s)
    sleep(0.001)
fout.close()
