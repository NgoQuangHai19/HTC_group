from Week3.RS485Controller import * 
from Week3.scheduler import *
from Week3.softwaretimer import * 
from Week3.Task1 import * 
from Week3.Task2 import * 
from Week3.read_sensor_task import *
from Week3.adafruit import *
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

