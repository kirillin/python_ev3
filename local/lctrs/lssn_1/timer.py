from ev3dev.auto import Screen
from time import sleep, time

lcd = Screen()
start_time = time()
while True:
    lcd.clear()
    lcd.draw.text((0, 10), str(start_time))
    lcd.draw.text((0,20), str(time() - start_time))
    lcd.update()
    sleep(0.043)
