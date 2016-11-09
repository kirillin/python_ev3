#!/usr/bin/env python
from ev3dev.auto import *
import time
import math
import AngleSensor

WAIT_TIME = 1
K_PSI =     -29.6
K_DPSI =    -0.55
K_DTHETA =  -5.8

motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
halt = Button()

angle = AngleSensor.Angle.get_obj()

offset_psi = 0
psi = 0

motorA.reset()
motorB.reset()
theta = motorA.position

Sound().beep()
time.sleep(0.5)

start_time = time.time()

while (True):
    max_voltage = PowerSupply().measured_volts

    if halt.enter:
        motorA.duty_cycle_sp = 0
        motorB.duty_cycle_sp = 0
        raise SystemExit


    last_psi = psi
    last_theta = theta

    psi = angle.get_angle() + 1

    if psi > 180:
        psi = psi - 360

    theta = motorA.position

    dtheta = (theta - last_theta) / WAIT_TIME
    dpsi = (psi - last_psi) / WAIT_TIME

    u = K_PSI * psi + K_DPSI * dpsi + K_DTHETA * dtheta
    u = u * 100 / max_voltage
    if abs(u) > 100:
        u = math.copysign(1, u) * 100
    motorA.run_direct(duty_cycle_sp=-u)
    motorB.run_direct(duty_cycle_sp=u)
    #time.sleep(WAIT_TIME)
    t = time.time() - start_time
    print(t)