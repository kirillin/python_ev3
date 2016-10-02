from ev3dev.auto import *
import ev3dev.ev3 as ev3
import time

typeMotor = ["LargeMotor", "MiddleMotor"]
whatMotor = ["black", "blue"]
tM = 0
wM = 0
power = 40
cycles = 1000

fileName = "data%s_%s_%dpwr_%dsec.txt" % (typeMotor[tM], whatMotor[wM], power, cycles)

fout = open(fileName, "w")
m = ev3.LargeMotor(ev3.OUTPUT_A)
m.reset()
m.duty_cycle_sp = power
m.run_forever()
t_start = time.time()
for i in range(0, cycles):
    t = time.time() - t_start
    angle = m.position
    line = '%f\t%d\n' % (t, angle)
    fout.write(line);
    time.sleep(0.0005)
fout.close()

