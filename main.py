import sys
import time
from scheduler import *
from physical import *
from week2 import *
from task1 import * 
from task2 import * 
from task3 import * 


scheduler = Scheduler()
scheduler.SCH_Init()

task1a = Task1()
task1b = Task2()
task1c = Task3()
task1d = Task1()


scheduler.SCH_Add_Task(task1d.Task1_Run, 10000,0)
scheduler.SCH_Add_Task(task1a.Task1_Run, 10000,0)
scheduler.SCH_Add_Task(task1b.Task2_Run, 3000,5000)
scheduler.SCH_Add_Task(task1c.Task3_Run, 4000,5000)


while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

