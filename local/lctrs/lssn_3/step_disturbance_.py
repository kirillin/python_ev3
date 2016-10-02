from ev3dev.auto import *
import ev3dev.ev3 as ev3
import time

m = ev3.LargeMotor(ev3.OUTPUT_A)
typeMotor = ["LargeMotor", "MiddleMotor"]
whatMotor = ["black", "blue"]
tM = 0
wM = 0
pwr = [7, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
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
