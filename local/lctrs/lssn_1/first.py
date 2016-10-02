#!/usr/bin/python
import ev3dev.ev3 as ev3

motor = ev3.LargeMotor(ev3.OUTPUT_A)
motor.run_timed(speed_sp=360, time_sp=1000, stop_action="brake")