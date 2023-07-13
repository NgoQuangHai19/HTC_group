# from tkinter import *
# import tkinter as tk
 
# class Example(Frame):
#    def __init__(self, parent):
#        Frame.__init__(self, parent)
#        self.parent = parent
#        self.initUI()
  
#    def initUI(self):
#        self.parent.title("Lines")
#        self.pack(fill=BOTH, expand=1)
  
#        img = PhotoImage(file="Images/hcmut_logo.png")
       
#        canvas = Canvas(self)
#        canvas.create_line(15, 25, 200, 25)
#        canvas.create_line(300, 25, 300, 200, dash=(4, 2))
#        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
  
#        canvas.pack(fill=BOTH, expand=1)
    
# root = Tk()
# ex = Example(root)
# root.geometry("400x250+300+300")

# root.mainloop()


from tkinter import *
import tkinter as tk

class SensorUI(tk.Tk):
    dataModel = None

    def __init__(self):
        super().__init__()
        self.title("Sensor UI")
        self.geometry("500x200")
        self.configure(bg="#F0F0F0")
        self.resizable(False, False)

        self.sensor1_label = tk.Label(self, text="Sensor 1 Value: 0", font=("Arial", 15), bg="#F0F0F0")
        self.sensor1_label.place(x=0, y=0)

        # self.sensor2_label = tk.Label(self, text="Sensor 2 Value: 0", font=("Arial", 15), bg="#F0F0F0")
        # self.sensor2_label.place(x=0, y=30)

        # self.photo = PhotoImage(file="Images/off_button.jpeg")

        self.relay1_label = tk.Label(self, text="The relay 1 is off", font=("Arial", 15), bg="#D50000", activebackground="#D50000")
        self.relay1_label.place(x=0, y=60)

        self.relay1_button = tk.Button(self, text="Turn On", font=("Arial", 15), bg="#428df5", command=self.toggle_relay1)
        self.relay1_button.place(x=300, y=60)

        self.relay2_label = tk.Label(self, text="The relay 2 is off", font=("Arial", 15), bg="#D50000", activebackground="#D50000")
        self.relay2_label.place(x=0, y=90)

        self.relay2_button = tk.Button(self, text="Turn On", font=("Arial", 15), bg="#428df5", command=self.toggle_relay2)
        self.relay2_button.place(x=300, y=90)

        self.relay_on = False

        self.update_sensor_values()        

    def toggle_relay1(self):
        self.relay_on = not self.relay_on
        if self.relay_on:
            self.relay1_button.config(text="Turn Off", bg="#D50000", activebackground="#00FFFF")
            self.relay1_label.config(text="The relay 1 is on", bg="#4CAF50", activebackground="#22e32b")
            #code bật thiết bị 1
            
        else:
            self.relay1_button.config(text="Turn On", bg="#4CAF50", activebackground="#22e32b")
            self.relay1_label.config(text="The relay 1 is off", bg="#D50000", activebackground="#b71c1c")
            #code tắt thiết bị 1


    def toggle_relay2(self):
        self.relay_on = not self.relay_on
        if self.relay_on:
            self.relay2_button.config(text="Turn Off", bg="#D50000", activebackground="#00FFFF")
            self.relay2_label.config(text="The relay 2 is on", bg="#4CAF50", activebackground="#22e32b")
            #code bật thiết bị 2
        
        else:
            self.relay2_button.config(text="Turn On", bg="#4CAF50", activebackground="#22e32b")
            self.relay2_label.config(text="The relay 2 is off", bg="#D50000", activebackground="#b71c1c")
            #code tắt thiết bị 2


    # def update_sensor_value(self):
    #     sensor1_value = 100
    #     sensor2_value = 20
    #     self.sensor1_label.config(text="Sensor 1 Value: {}".format(sensor1_value))
    #     self.sensor2_label.config(text="Sensor 2 Value: {}".format(sensor2_value))
    #     self.after(10000, self.update_sensor_value)
    def update_sensor_values(self):
        if self.relay_on:
            # Code to read sensor values
            sensor1_value = 10
            # sensor2_value = 20
        else:
            sensor1_value = 0
            # sensor2_value = 0

        self.sensor1_label.config(text="Sensor 1 Value: {}".format(sensor1_value))
        # self.sensor2_label.config(text="Sensor 2 Value: {}".format(sensor2_value))

        self.after(10000, self.update_sensor_values)  # Schedule the next update after 10 seconds (10000 milliseconds)


if __name__ == "__main__":
    app = SensorUI()
    app.mainloop()
