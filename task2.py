import sys
import time
from scheduler import *
from task2 import *
from task1 import *



scheduler = Scheduler()
scheduler.SCH_Init()

task1a = Task1()
task1b = Task1()

scheduler.SCH_Add_Task(task1a.Task1_Run, 1000,5000)
scheduler.SCH_Add_Task(task1b.Task1_Run, 3000,5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)