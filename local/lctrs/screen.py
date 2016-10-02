#!/usr/bin/python
from PIL import Image, ImageFont
from ev3dev.auto import *
import time
import sys
from subprocess import call
"""
    178x128
"""

lcd = Screen()
lcd.clear()

print(lcd.xres)     #разрешение экрана по x. тип Long
print(lcd.yres)     #разрешение экрана по y. тип Long
print(lcd.shape)    #разрешение по xy. тип Tuple

lcd.draw.arc((20, 80, 158, 100), 0, 180) #дуга
lcd.draw.ellipse(( 20, 20,  60, 60))    #окружность
lcd.draw.rectangle((0,0,177,40))        #прямоугольник
lcd.draw.rectangle((0,50,177,0), fill='black') #закрашенный прямоугольник
lcd.draw.text((48,20),'Hello, world.', fill='white') #белай надпись на черном прямоугольнике
lcd.draw.text((36,80),'THIS TEXT IS BLACK', spacing=10, align="left")
lcd.draw.line((10,10,178,128),5)
lcd.draw.pieslice((50,50,100,100),0, 45)    #долька пирога
lcd.draw.point((56,56))
lcd.draw.chord((10,10,178,128), 0, 199)


#на роботе sudo apt-get install ttf-mscorefonts-installer
path = "/usr/share/fonts/truetype/msttcorefonts/Courier_New.ttf"
f = ImageFont.truetype(path, 18)
lcd.draw.text((0, 0), "Im EV3!", font=f)

#на удал. машине scp /media/data/1.jpg robot@ev3dev:/home/robot/
#logo = Image.open('/home/robot/1.jpg')
#lcd.image.paste(logo, (0,0))

#how do screenshot
screenshot = "screenshot"
out_name = sys.argv[1] if len(sys.argv) > 1 else screenshot

call(["fbgrab", out_name]);

image = Image.open(out_name)
image = image.convert("RGB")
image = image.resize(tuple(i * 2 for i in image.size), Image.NEAREST)

pixel_data = image.load()

for y in range(image.size[1]):
    for x in range(image.size[0]):
        if pixel_data[x, y] == (255, 255, 255):
            pixel_data[x, y] = (173, 181, 120)

image.save(out_name);




lcd.update()
time.sleep(2)