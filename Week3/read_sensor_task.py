from RS485Controller import *
from adafruit import *
import time

class ReadSensorTask:
    def __init__(self, _rs485):
        self.rs485=_rs485
        self.client=Adafruit(AIO_USERNAME, AIO_KEY, AIO_FEED_ID)
        self.client.connect() 
        
    def setDevice1On(self):
        # if state == 1:
        #     print("Read relay 1")
        # elif state == 0 :
        #     print("Write relay 1")
        state=self.rs485.setDevice1(1)
        print("Trang thai cua relay: ",state)
        #self.client.mqtt_client.publish(AIO_FEED_ID[1],state)

    def setDevice1Off(self):
        # if state == 1:
        #     print("Read relay 1")
        # elif state == 0 :
        #     print("Write relay 1")
        state=self.rs485.setDevice1(1)
        print("Trang thai cua relay: ",state)
        #self.client.mqtt_client.publish(AIO_FEED_ID[1],state)
    
    def setDevice2(self, state):
        if state == 1:
            print("Read relay 1")
        elif state == 0 :
            print("Write relay 1")
        self.rs485.setDevice2(state)

    def readValueDistance(self):
        # if number == 9:
        #     print("Get value of distance sensor 9")
        # elif number == 12 :
        #     print("Get value of distance sensor 12")
        distance=self.rs485.getvalueDistance(12)
        print("Khoang cach la: ",distance)
        self.client.mqtt_client.publish(AIO_FEED_ID[2],distance)
    
#task1 = ReadSensorTask()
# while(True):
#     time.sleep(1)






