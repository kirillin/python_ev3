from datetime import datetime
import os

path = "/media/data/evo/tests/"
#cmdpy3_0 = "pyton3 output.py"
#cmdpy0 = "pyton output.py"
cmdcpp = "./a.out"
cmdpy = "a.py"

arr = {"cpp": cmdcpp, "py": cmdpy}


t = datetime.timestamp(datetime.now())
os.system(path + arr["cpp"])
dt = datetime.timestamp(datetime.now()) - t
print("cpp: " + str(dt))

t = datetime.timestamp(datetime.now())
os.system(path + arr["py"])
dt = datetime.timestamp(datetime.now()) - t
print("py: " + str(dt))