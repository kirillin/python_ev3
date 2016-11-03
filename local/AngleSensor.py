from ev3dev.auto import *
import itertools
import os
import pyudev

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

    def get_data(self, interval):
        angle_raw = self.get_angle()
        return angle_raw