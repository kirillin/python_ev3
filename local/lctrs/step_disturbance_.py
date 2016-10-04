#!/usr/bin/env python
from ev3dev.auto import *
import ev3dev.ev3 as ev3
import time

"""
    !!! ВОЗМОЖНО УЖЕ НЕ РАБОТАЕТ, ИБО метод run_forever
    с какой-то версии библиотеки управляется не ШИМом,
    а скоростью поворота в град./с

    Усовершенствованная версия программы lssn_3/motor_ind_py
    Снимает показания с двигателя от 0 до 100 с шагом 5
    Сохраняет файл со значением времени и углома поврота
    для каждого из шагов
"""

m = ev3.LargeMotor(ev3.OUTPUT_A)
typeMotor = ["LargeMotor", "MiddleMotor"]
whatMotor = ["black", "blue"]
tM = 0
wM = 0
pwr = [i for i in range(0, 101, 5)]
cycles = 1000

for p in range(0, len(pwr)):
    power = pwr[p]
    fileName = "data%s_%s_%dpwr_%dsec.txt" % (typeMotor[tM], whatMotor[wM], power, cycles)
    fout = open(fileName, "w")
    m.reset()
    m.duty_cycle_sp = power
    time.sleep(3);
    m.run_forever()
    t_start = time.time()
    for i in range(0, cycles):
        t = time.time() - t_start
        angle = m.position
        line = '%f\t%d\n' % (t, angle)
        fout.write(line);
        time.sleep(0.0005)
    fout.close()
    m.stop();
    print("Power is " + str(power))
print("The end!")
