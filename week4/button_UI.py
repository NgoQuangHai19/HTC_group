import tkinter as tk
import serial.tools.list_ports
import time

relay_ON = [[0, 0, 0, 0, 0, 0, 0, 0],
            [1, 6, 0, 0, 0, 255, 201, 138],
            [2, 6, 0, 0, 0, 255, 201, 185],
            [3, 6, 0, 0, 0, 255, 200, 104],
            [4, 6, 0, 0, 0, 255, 201, 223],
            [5, 6, 0, 0, 0, 255, 200, 14],
            [6, 6, 0, 0, 0, 255, 200, 61],
            [7, 6, 0, 0, 0, 255, 201, 236],
            [8, 6, 0, 0, 0, 255, 201, 19]]

relay_OFF = [[0, 0, 0, 0, 0, 0, 0, 0],
             [1, 6, 0, 0, 0, 0, 137, 202],
             [2, 6, 0, 0, 0, 0, 137, 249],
             [3, 6, 0, 0, 0, 0, 136, 40],
             [4, 6, 0, 0, 0, 0, 137, 159],
             [5, 6, 0, 0, 0, 0, 136, 78],
             [6, 6, 0, 0, 0, 0, 136, 125],
             [7, 6, 0, 0, 0, 0, 137, 172],
             [8, 6, 0, 0, 0, 0, 137, 83]]
port = "/dev/ttyAMA2"
baudrate = 9600
print("Find port {} - baudrate {}".format(port, baudrate))
"""ser = serial.Serial(port, baudrate, timeout=1, bytesize=8, parity="N",stopbits=1)"""
ser = serial.Serial(port, baudrate)
print(ser)


def serial_read_data(ser):
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        out = ser.read(bytesToRead)
        data_array = [b for b in out]
        print(data_array)
        if len(data_array) >= 7:
            array_size = len(data_array)                                                                                                            
            value = data_array[array_size - 4] * 256 + data_array[array_size - 3]                                                                   
            return value                                                                                                                            
        else:                                                                                                                                       
            return -1                                                                                                                               
    return 0                                                                                                                                        
                                                                                                                                                    
                                                                                                                                                    
class CustomTkinter(tk.Tk):                                                                                                                         
    def __init__(self):                                                                                                                             
        super().__init__()                                                                                                                          
        self.title("Custom Window")                                                                                                                 
        self.geometry("500x500")                                                                                                                    
                                                                                                                                                    
        self.switches = []                                                                                                                          
        for i in range(8):                                                                                                                          
            switch_frame = tk.Frame(self)                                                                                                           
            switch_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=10, pady=10)                                                                          
                                                                                                                                                    
            switch_label = tk.Label(switch_frame, text=f"Switch {i + 1}")                                                                           
            switch_label.pack(side=tk.LEFT)                                                                                                         
                                                                                                                                                    
            switch_button = tk.Button(switch_frame, text="Off", command=lambda i=i: self.toggle_switch(i), width=20,                                
                                      height=2)                                                                                                     
            switch_button.pack(side=tk.RIGHT)                                                                                                       
                                                                                                                                                    
            self.switches.append({"button": switch_button, "status": False})                                                                        
            self.switches[i]["button"].config(text="Off", bg="red")                                                                                 
                                                                                                                                                    
    def toggle_switch(self, i):                                                                                                                     
        self.switches[i]["status"] = not self.switches[i]["status"]                                                                                 
        if self.switches[i]["status"]:                                                                                                              
            self.switches[i]["button"].config(text="On", bg="green")                                                                                
            print("Test ON relay ID=", i + 1)                                                                                                       
            ser.write(relay_ON[i + 1])                                                                                                              
            serial_read_data(ser)                                                                                                                   
        else:                                                                                                                                       
            self.switches[i]["button"].config(text="Off", bg="red")                                                                                 
            print("Test OFF relay ID=", i + 1)                                                                                                      
            ser.write(relay_OFF[i + 1])                                                                                                             
            serial_read_data(ser)                                                                                                                   
                                                                                                                                                    
                                                                                                                                                    
window = CustomTkinter()        