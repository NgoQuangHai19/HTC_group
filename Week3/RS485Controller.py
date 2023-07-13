import time
import serial.tools.list_ports 

class RS485Controller:
    def __init__(self):
        self.ser = None
        self.portName = self.getPort()
        if self.portName != "None":
            self.ser = serial.Serial(port=self.portName, baudrate=9600)
    
    def getPort(self):
        ports = serial.tools.list_ports.comports()
        N = len(ports)
        commPort = "None"
        for i in range(0, N):
            port = ports[i]
            strPort = str(port)
            print(strPort) # print(strPort)
            if "/dev/ttyAMA2" in strPort:
                splitPort = strPort.split(" ")
                print("PortName:", strPort)
                commPort = splitPort[0]
        return commPort
    
    def setDevice1(self, state):
        relay1_ON = [0, 6, 0, 0, 0, 255, 200, 91]
        relay1_OFF = [0, 6, 0, 0, 0, 0, 136, 27]
        if state:
            print("Bat relay 1")
            self.ser.write(relay1_ON)
            # client.publish(AIO_FEED_ID[2], 1)
        else:
            print("Tat relay 1")
            self.ser.write(relay1_OFF)
            # client.publish(AIO_FEED_ID[2], 0)
        state = self.serial_read_data()
        
    
    def setDevice2(self, state):
        relay2_ON = [15, 6, 0, 0, 0, 255, 200, 164]
        relay2_OFF = [15, 6, 0, 0, 0, 0, 136, 228]
        self.serial_read_data()
        if state:
            self.ser.write(relay2_ON)
            # client.publish(AIO_FEED_ID[3], 1)
        else:
            self.ser.write(relay2_OFF)
            # client.publish(AIO_FEED_ID[3], 0)
    
    def serial_read_data(self):
        bytesToRead = self.ser.inWaiting()
        if bytesToRead > 0:
            out = self.ser.read(bytesToRead)
            data_array = [b for b in out]
            print(data_array)
            if len(data_array) >= 7:
                array_size = len(data_array)
                value = data_array[array_size - 4] * 256 + data_array[array_size - 3]
                return value
            else:
                return -1
        return 0
    
    def relayController(self, number, state):
        relay_ON =  [[1, 6, 0, 0, 0, 255, 201, 138],
                     [2, 6, 0, 0, 0, 255, 201, 185],
                     [3, 6, 0, 0, 0, 255, 200, 104],
                     [4, 6, 0, 0, 0, 255, 201, 223],
                     [5, 6, 0, 0, 0, 255, 200, 14],
                     [6, 6, 0, 0, 0, 255, 200, 61],
                     [7, 6, 0, 0, 0, 255, 201, 236],
                     [8, 6, 0, 0, 0, 255, 201, 19]]
    
        relay_OFF = [[1, 6, 0, 0, 0, 0, 137, 202],
                     [2, 6, 0, 0, 0, 0, 137, 249],
                     [3, 6, 0, 0, 0, 0, 136, 40],
                     [4, 6, 0, 0, 0, 0, 137, 159],
                     [5, 6, 0, 0, 0, 0, 136, 78],
                     [6, 6, 0, 0, 0, 0, 136, 125],
                     [7, 6, 0, 0, 0, 0, 137, 172],
                     [8, 6, 0, 0, 0, 0, 137, 83]]
        
        if state == 0:
            self.ser.write(relay_OFF[number - 1])
            print(self.serial_read_data())
        else:
            self.ser.write(relay_ON[number - 1])
            print(self.serial_read_data())
    
    def getvalueDistance(self, number):
        distance_9 = [9, 3, 0, 5, 0, 1, 149, 67]
        distance_12 = [12, 3, 0, 5, 0, 1, 149, 22]
        
        if number == 9:
            self.ser.write(distance_9)
            distance = self.serial_read_data()
        elif number == 12:
            self.ser.write(distance_12)
            distance = self.serial_read_data()
        else:
            print("The input gate is entered incorrectly")
        return distance
        


