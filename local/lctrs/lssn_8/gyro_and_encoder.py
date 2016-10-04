#!/usr/bin/env python3
from ev3dev.auto import TouchSensor, GyroSensor, LargeMotor, OUTPUT_A, INPUT_1
from time import sleep

motor = LargeMotor(OUTPUT_A)
gyro = GyroSensor(INPUT_1)

button1 = TouchSensor("in3")
button2 = TouchSensor("in4")

motor.reset()
gyro.mode = gyro.modes[0]

offset = gyro.value()

i = 0
flag = True
while True:
    if (button1.value() == True):
        i = i + 1
        flag = True
    if (button2.value() == True):
        i = i - 1
        flag = True
    if (flag == True):
        motor.run_to_rel_pos(speed_sp=100, position_sp=i, stop_action="hold")
        flag = False
    mangle = motor.position
    gangle = gyro.value() - offset
    line = "%d = %d" % (mangle, gangle)
    print(line)
    i = 0
    sleep(0.001)