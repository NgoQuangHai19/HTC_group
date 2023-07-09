import sys
import time
from Week3.adafruit import *
# from Week3.RS485Controller import * 
from Week3.scheduler import *
from Week3.softwaretimer import * 
from Week3.Task1 import * 
from Week3.Task2 import * 
###


scheduler = Scheduler()
scheduler.SCH_Init()

task1a = Task1()
task1b = Task2()
task1c = Task2()


scheduler.SCH_Add_Task(task1a.Task1_Run, 10000,0)
scheduler.SCH_Add_Task(task1b.Task2_Run, 3000,5000)
scheduler.SCH_Add_Task(task1c.Task2_Run, 4000,5000)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

