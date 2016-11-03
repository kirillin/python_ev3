#!/usr/bin/env python
from ev3dev.auto import *
import time
import math
import AngleSensor

WAIT_TIME = 0.01
K_PSI = -51.7
K_DPSI = -0.68
K_DTHETA = -10.4

file_name = 'data.txt'
fout = open(file_name, "w")

motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
halt = Button();
#gyro = GyroSensor(INPUT_1)
#gyro.mode = 'GYRO-RATE'
#gyro.mode = 'GYRO-ANG'
angle = AngleSensor.Angle.get_obj()

offset_psi = 0
psi = 0

motorA.reset()
motorB.reset()

theta = motorA.position

Sound().beep()

time.sleep(0.5)

while (True):
    if halt.enter:
        motorA.duty_cycle_sp = 0
        motorB.duty_cycle_sp = 0
        raise SystemExit
    max_voltage = PowerSupply().measured_volts
    last_psi = psi
    last_theta = theta

    psi = angle.get_angle() +1 #- offset_psi#gyro.value()
    if psi > 180:
        psi = psi - 360
    theta = motorA.position

    dtheta = (theta - last_theta);
    dpsi = (psi - last_psi);


    #fout.write(line)
    #print(line)
    u = K_PSI * psi + K_DPSI * dpsi + K_DTHETA * dtheta
    line = '%f\t%d\t%d\t%d\n' % (t, psi, dpsi, u)
    #u = u * 100 / max_voltage
    print(line)
    if abs(u) > 100:
        u = math.copysign(1, u) * 100
    motorA.run_direct(duty_cycle_sp=-u)
    motorB.run_direct(duty_cycle_sp=u)

    time.sleep(WAIT_TIME)