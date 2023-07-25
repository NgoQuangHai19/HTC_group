import tkinter as tk
from tkinter import *
import time
from PIL import Image
from RS485Controller import RS485Controller
from read_sensor_task import *



class Main_UI:
    dataModel = None
    numberButton = 8
    

    def __init__(self,data):
        self.dataModel = data
        print("Init the UI!!")
        
        self.window = tk.Tk()
        self.on = PhotoImage(file="on2.png")
        self.off = PhotoImage(file="off2.png")

        self.is_on = [False, False, False, False, False, False, False, False]
        self.on_button = []
        for i in range(0, self.numberButton):
            self.on_button.append(Button(self.window, bd=0, justify=RIGHT))

        self.window.attributes('-fullscreen', True)
        self.window.title("Control Panel")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        print("Size = ", screen_width, screen_height)

        
        self.intro = tk.Label(text="Control Panel",
                              fg="#000",
                              justify=CENTER,
                              font="Helvetica 50 bold")
        self.intro.place(x=screen_width/3 , y=0, width=screen_width/3, height=100)

        self.on_button[0] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(1))
        self.on_button[0].place(x=screen_width/4 + 55 , y=210)
        self.Relay1 = Label(self.window, text="Relay 1",fg="#000", font= "Helvetica 50 bold")
        self.Relay1.place(x=55, y=210, width=screen_width/4, height=100)

        self.on_button[1] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(2))
        self.on_button[1].place(x=3* screen_width / 4 + 55, y=210)
        self.Relay2 = Label(self.window, text="Relay 2", fg="#000", font="Helvetica 50 bold")
        self.Relay2.place(x=2* screen_width / 4 + 55, y=210, width=screen_width / 4, height=100)

        self.on_button[2] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(3))
        self.on_button[2].place(x=screen_width / 4 + 55, y=310)
        self.Relay3 = Label(self.window, text="Relay 3", fg="#000", font="Helvetica 50 bold")
        self.Relay3.place(x=55, y=310, width=screen_width / 4, height=100)

        self.on_button[3] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(4))
        self.on_button[3].place(x=3*screen_width / 4 + 55, y=310)
        self.Relay4 = Label(self.window, text="Relay 4", fg="#000", font="Helvetica 50 bold")
        self.Relay4.place(x=2*screen_width / 4 + 55, y=310, width=screen_width / 4, height=100)

        self.on_button[4] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(5))
        self.on_button[4].place(x=screen_width / 4 + 55, y=410)
        self.Relay5 = Label(self.window, text="Relay 5", fg="#000", font="Helvetica 50 bold")
        self.Relay5.place(x=55, y=410, width=screen_width / 4, height=100)

        self.on_button[5] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(6))
        self.on_button[5].place(x=3*screen_width / 4 + 55, y=410)
        self.Relay6 = Label(self.window, text="Relay 6", fg="#000", font="Helvetica 50 bold")
        self.Relay6.place(x=2*screen_width / 4 + 55, y=410, width=screen_width / 4, height=100)

        self.on_button[6] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(7))
        self.on_button[6].place(x=screen_width / 4 + 55, y=510)
        self.Relay7 = Label(self.window, text="Relay 7", fg="#000", font="Helvetica 50 bold")
        self.Relay7.place(x=55, y=510, width=screen_width / 4, height=100)

        self.on_button[7] = Button(self.window, image=self.off, bd=0, command=lambda :self.toggle_button_click(8))
        self.on_button[7].place(x=3*screen_width / 4 + 55, y=510)
        self.Relay8 = Label(self.window, text="Relay 8", fg="#000", font="Helvetica 50 bold")
        self.Relay8.place(x=2*screen_width / 4 + 55, y=510, width=screen_width / 4, height=100)


        self.labelDistance1 = tk.Label(text="Distance1",
                                        fg="#000",
                                        font="Helvetica 50 bold")

        self.labelDistance1.place(x=30, y=610, width=screen_width / 3, height=100)


        self.labelDistance1Value = tk.Label(text="2000",
                                           fg="#000",
                                           font="Helvetica 50 bold")

        self.labelDistance1Value.place(x=2*screen_width / 4 - 50, y=610, width=screen_width / 3, height=100)

        self.labelDistance1Unit = tk.Label(text="mm",
                                           fg="#000",
                                           font="Helvetica 50 bold")

        self.labelDistance1Unit.place(x=2*screen_width / 4 + 300, y=610, width=screen_width / 4, height=100)

        self.labelDistance2 = tk.Label(text="Distance2",
                                       fg="#000",
                                       font="Helvetica 50 bold")

        self.labelDistance2.place(x=30, y=710, width=screen_width / 3, height=100)


        self.labelDistance2Value = tk.Label(text="2000",
                                            fg="#000",
                                            font="Helvetica 50 bold") 

        self.labelDistance2Value.place(x=2*screen_width / 4 - 50, y=710, width=screen_width / 3, height=100)

        self.labelDistance1Unit = tk.Label(text="mm",
                                           fg="#000",
                                           font="Helvetica 50 bold")

        self.labelDistance1Unit.place(x=2*screen_width / 4 + 300, y=710, width=screen_width / 4, height=100)

    def control_relay(self, number, state):
        if state == 1:
            self.dataModel.relayController(number, 1)
            print("Relay {} is ON".format(number))
        elif state == 0:
            self.dataModel.relayController(number, 0)
            print("Relay {} is OFF".format(number))

    def toggle_button_click(self, number):
        if self.is_on[number - 1]:
            self.UI_Set_Button_text(number, self.off)
            self.is_on[number - 1] = False
            self.control_relay(number, 0)
        else:
            self.UI_Set_Button_text(number, self.on)
            self.is_on[number - 1] = True
            self.control_relay(number, 1)
    
    def UI_Refresh(self):
        self.UI_Set_Value_Text(self.labelDistance1Value, self.dataModel.getvalueDistance(9))
        self.UI_Set_Value_Text(self.labelDistance2Value, self.dataModel.getvalueDistance(12))
        for i in range(0, self.numberButton - 1 ) :
            if self.dataModel.BUTTON_STATE[i] == True:
                self.on_button[i].config(image = self.on)
                self.is_on=True
            else:
                self.on_button[i].config(image = self.off)
                self.is_on=False
        self.window.update()

    def UI_Set_Value_Text(self, text_object, data):
        text_object.config(text="%.2f" %data)

    def UI_Set_Button_text(self, number, data):
        if number == 1:
            self.on_button[0].config(image= data)
        elif number == 2:
            self.on_button[1].config(image= data)
        elif number == 3:
            self.on_button[2].config(image= data)
        elif number == 4:
            self.on_button[3].config(image= data)
        elif number == 5:
            self.on_button[4].config(image= data)
        elif number == 6:
            self.on_button[5].config(image= data)
        elif number == 7:
            self.on_button[6].config(image= data)
        elif number == 8:
            self.on_button[7].config(image= data)

if __name__ == "__main__":
    ser=RS485Controller()
    app = Main_UI(ser)
    app.UI_Refresh()
    app.window.mainloop()

