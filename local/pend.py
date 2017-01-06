#!/usr/bin/env python3
from ev3dev.auto import LargeMotor, Button
import itertools
import os
import time
import pyudev
import math


WAIT_TIME = 0.05
K_PSI =     -39
K_DPSI =    -0.07
K_DTHETA =  -8

WHEEL_RATIO_NXT1 = 1.0 # 56mm
WHEEL_RATIO_NXT = 0.8 # 43.2mm (same as EV3)
WHEEL_RATIO_RCX = 1.4 # 81.6mm

KGYROANGLE = 7.5
KGYROSPEED = 1.15
KPOS = 0.07
KSPEED = 0.1

KDRIVE = -0.02

KSTEER = 0.25

TIME_FALL_LIMIT = 3 #0.5

EMAOFFSET = 0.0005

class Angle:
    @staticmethod
    def get_obj():
        devices = list(pyudev.Context().list_devices(subsystem='lego-sensor').match_property("LEGO_DRIVER_NAME", 'ht-nxt-angle'))

        if not devices:
            raise Exception('Angle not found')

        if devices[0].attributes['driver_name'] == b'ht-nxt-angle':
            return HTAngle(devices[0])

    def __init__(self, device):
        self.device = device
        self.value0 = open(os.path.join(self.device.sys_path, 'value0'), 'r')

    def set_mode(self, value):
        with open(os.path.join(self.device.sys_path, 'mode'), 'w') as f:
            f.write(str(value))

    def get_angle(self):
        self.value0.seek(0)
        return int(self.value0.read())

class HTAngle(Angle):
    def __init__(self, device):
        Angle.__init__(self, device)
        self.set_mode("ANGLE")
        self.speed_angle = 0.0
        self.current_angle = 0.0
        self.prev_angle = 0
        self.prev_deltas = [0, 0, 0]

    def get_data(self, interval):
        angle_raw = self.get_angle() + 1
        self.current_angle = angle_raw
        delta = self.current_angle - self.prev_angle
        self.speed_angle = (delta + sum(self.prev_deltas)) / (4 * interval)
        self.prev_angle = self.current_angle
        self.prev_deltas = [delta] + self.prev_deltas[0:2]
        return self.speed_angle, self.current_angle

class EV3Motors:
    def __init__(self, left=0, right=1):
        self.left = LargeMotor('outA')
        self.right = LargeMotor('outB')
        self.pos = 0.0
        self.speed = 0.0
        self.diff = 0
        self.target_diff = 0
        self.drive = 0
        self.steer = 0
        self.prev_sum = 0
        self.prev_deltas = [0,0,0]

    def get_data(self, interval):
        left_pos = self.left.position
        right_pos = self.right.position

        pos_sum = right_pos + left_pos
        self.diff = left_pos - right_pos

        delta = pos_sum - self.prev_sum
        self.pos += delta

        self.speed = (delta + sum(self.prev_deltas)) / (4 * interval)

        self.prev_sum = pos_sum
        self.prev_deltas = [delta] + self.prev_deltas[0:2]

        return self.speed, self.pos

    def go(self):
        self.left.run_direct()
        self.right.run_direct()

    def stop(self):
        self.left.stop()
        self.right.stop()

    def set_power(self, power):
        self.left.duty_cycle_sp = -power
        self.right.duty_cycle_sp = power

wheel_ratio = WHEEL_RATIO_NXT1

a = HTAngle.get_obj()
halt = Button()

os.system("beep -f 440 -l 10")
time.sleep(1)
motors = EV3Motors()
start_time = time.time()
last_okay_time = start_time
avg_interval = 0.0055
motors.go()
for loop_count in itertools.count():
    if halt.enter:
        motors.stop()
        raise SystemExit

    angle_speed, angle = a.get_data(avg_interval)
    motors_speed, motors_pos = motors.get_data(avg_interval)

    motors_pos -= motors.drive * avg_interval
    motors.pos = motors_pos
    if angle > 180:
        angle = angle - 360
    power =   K_PSI * angle\
            + K_DPSI * angle_speed\
            + K_DTHETA * motors_speed

    # left_power, right_power = motors.steer_control(power, 0, avg_interval)
    if abs(power) > 100:
        power = math.copysign(1, power) * 100
    power = math.trunc(power)
    # line = "%f\t%f\t%f\t%d" % (angle, angle_speed, motors_speed, power)
    # print(line)
    #print left_power, right_power

    motors.set_power(power)

    time.sleep(WAIT_TIME+avg_interval)

    now_time = time.time()
    avg_interval = (now_time - start_time) / (loop_count+1)
    #print(avg_interval)
