import ev3dev.ev3 as ev3
import math
import time

GYRO_PORT = ev3.INPUT_1
LEFT_MOTOR = ev3.OUTPUT_A
RIGHT_MOTOR = ev3.OUTPUT_B
WAIT_TIME = 0.008
KGYROANGLE = 45
KSPEED = 1.38
KGYROSPEED = 10
KPOS = 0.5
JUST_WAIT = 1
KGYROINT = 20

sign = lambda x: math.copysign(1, x)

t = WAIT_TIME * 0.001
segway_angle = 0
wheel_angle = 0
last_wheel_angle = 0
wheel_speed = 0
u = 0
int_segway_angle = 0

motor_right = ev3.LargeMotor(RIGHT_MOTOR)
motor_left = ev3.LargeMotor(LEFT_MOTOR)

gyro = ev3.GyroSensor(GYRO_PORT)
gyro.mode = 'GYRO-RATE'
gyro.mode = 'GYRO-ANG'
offset = gyro.value()

print(offset)

while True:
    max_voltage = ev3.PowerSupply().measured_volts
    segway_speed = (gyro.value() - offset) * math.pi / 180
    segway_angle += segway_speed * t
    int_segway_angle += segway_angle * t
    u = KGYROANGLE * segway_angle + KGYROSPEED * segway_speed + KGYROINT * int_segway_angle
    u = u * 100 / max_voltage
    if abs(u) > 100:
        u = math.copysign(1, u) * 100
    print(u)
    motor_left.duty_cycle_sp = u
    motor_right.duty_cycle_sp = u
    motor_right.run_forever()
    motor_left.run_forever()
    time.sleep(WAIT_TIME)