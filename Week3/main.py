import time
from scheduler import *
from softwaretimer import * 
from Task1 import *
from Task2 import *
scheduler = Scheduler()
scheduler.SCH_Init()

task1=Task1()   
task2=Task2()

scheduler.SCH_Add_Task(task1.Task1_Run,1000,0)
scheduler.SCH_Add_Task(task2.Task2_Run,3000,5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)