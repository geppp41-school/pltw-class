import datetime
import ctypes
from os import wait
from time import sleep
#https://stackoverflow.com/questions/10192903/time-in-milliseconds-in-c

time_lib = ctypes.CDLL('./computer-science-class/pltw-1.2.5/engine/time.so')
time_lib.getTimeMs.restype = ctypes.c_double

print(time_lib.getTimeMs())
sleep(0.1)
print(time_lib.getTimeMs())