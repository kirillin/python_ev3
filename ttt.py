import time

WAIT_TIME = 0.01

f = open('times.txt', 'w')

start_time = time.time()
while (True):
    t = time.time() - start_time
    f.write("%f\n" % (t* 1000))
    time.sleep(WAIT_TIME)
