#!/usr/bin/env python
from ev3dev.ev3 import LargeMotor, GyroSensor, \
    OUTPUT_A, INPUT_1, Sound, PowerSupply
from time import time, sleep
from math import pi, copysign

Kp = 15
pwr = 0

motor = LargeMotor(OUTPUT_A)
gyro = GyroSensor(INPUT_1)

battary = PowerSupply()
Sound().beep()
sleep(0.05)

motor.reset()
gyro.mode = gyro.modes[0]   #при выборе режима работы датчика значение сбрасывается в ноль

offset = gyro.value()
a = 0

start_time = time()
while True:
    t = time() - start_time
    rotation = motor.position
    angle = gyro.value() - offset
    a = a + angle * 0.001
    print("%d\t%d" % (angle, rotation))
    e = (90 - rotation) * pi / 180
    pwr = Kp * e
    pwr = pwr / battary.measured_volts * 90
    if abs(pwr) > 100:
        pwr = copysign(1, pwr) * 100
    motor.run_direct(duty_cycle_sp=pwr)
    sleep(0.001)

