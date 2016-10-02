#!/usr/bin/python
from ev3dev.auto import LargeMotor, Sound, OUTPUT_A
from time import sleep, time

sound = Sound()
motor = LargeMotor(OUTPUT_A)

sound.beep()
sleep(0.5)
motor.run_direct(duty_cycle_sp=50)
sleep(1)
sound.tone(500, 500)
sleep(0.5)

