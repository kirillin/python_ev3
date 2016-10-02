#!/usr/bin/python
from ev3dev.auto import LargeMotor, Screen, OUTPUT_A
from time import sleep

motor = LargeMotor(OUTPUT_A)
lcd = Screen()

motor.run_direct()
motor.duty_cycle_sp = 30
while True:
    lcd.clear()
    lcd.draw.text((0,10), "position is " + str(motor.position))
    lcd.update()
    sleep(0.042)
