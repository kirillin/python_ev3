import ev3dev.ev3 as ev3



m = ev3.LargeMotor(ev3.OUTPUT_A)
m.duty_cycle_sp = 30
m.time_sp = 10000
m.run_timed()
m.stop()