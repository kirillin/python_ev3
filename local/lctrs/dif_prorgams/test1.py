#!/usr/bin/python
from ev3dev.auto import LargeMotor, OUTPUT_A

motor = LargeMotor(OUTPUT_A)
motor.duty_cycle_sp = 80
motor.time_sp = 5000
motor.run_timed()   #should use speed_sp


