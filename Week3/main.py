from RS485Controller import * 
from scheduler import *
from softwaretimer import * 
from Task1 import * 
from Task2 import * 
from read_sensor_task import *
from adafruit import *
import sys
import time

###

ser  = RS485Controller()

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = ReadSensorTask(ser)

scheduler.SCH_Add_Task(task1.readValueDistance(9), 1000, 3000)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

