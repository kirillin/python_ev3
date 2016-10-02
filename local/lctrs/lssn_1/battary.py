#!/usr/bin/python
from ev3dev.auto import PowerSupply, Screen
from time import sleep

ps = PowerSupply()
voltage = ps.measured_voltage
volts = ps.measured_volts

lcd = Screen()
lcd.clear()
lcd.draw.text((0,10),"voltage is " + str(voltage))
lcd.draw.text((0,20),"volts is " + str(volts))
lcd.update()
sleep(5)