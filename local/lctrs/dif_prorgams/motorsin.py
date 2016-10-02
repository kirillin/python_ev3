from ev3dev.ev3 import LargeMotor, Sound, \
    GyroSensor, OUTPUT_A, INPUT_1
from time import sleep, time
from math import sin, pi

N = 1000

motor = LargeMotor(OUTPUT_A)
gyro = GyroSensor(INPUT_1)
Sound().beep()
fout = open("data.txt", "w")
sleep(1)
start_time = time()
for i in range(0, N):
    t = (time() - start_time) *1000
    rotation = gyro.value() + 4
    u_float = 100 * sin(pi * t / N)
    motor.run_forever(speed_sp = u_float*10)  #should use speed_sp!!!
    s = "%d\t%d\t%d" % (t, rotation, u_float)
    fout.write(s)
    sleep(0.004)
fout.close()