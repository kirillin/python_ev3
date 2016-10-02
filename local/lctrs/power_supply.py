from ev3dev.auto import PowerSupply
import ev3dev.ev3 as ev3

powerSupply = ev3.PowerSupply()

powerSupply.measured_voltage
powerSupply.measured_current

motor_left.duty_cycle_sp = u
motor_right.duty_cycle_sp = u
motor_right.run_forever()
motor_left.run_forever()