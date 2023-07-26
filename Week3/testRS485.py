# First, import the RS485Controller class
from RS485Controller import * 
import time

controller = RS485Controller()
controller.relayController(1, state=1)
time.sleep(1)
controller.relayController(1, state=0)
time.sleep(1)
while True:
    time.sleep(2)
    distance_9 = controller.getvalueDistance(9)
    print(f"Distance from sensor 9: {distance_9}")
    time.sleep(1.5)
    distance_12 = controller.getvalueDistance(12)
    print(f"Distance from sensor 12: {distance_12}")
    time.sleep(1.5)
