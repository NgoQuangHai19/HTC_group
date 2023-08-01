import customtkinter
import os
from PIL import Image
import cv2
import numpy as np
import requests
import time

from PIL import ImageOps
from PIL import Image, ImageTk
import threading


class App(customtkinter.CTk):
    numberButton=8
    def __init__(self, data):
        super().__init__()
        self.dataModel = data
        self.title("image_example.py")
        self.geometry("1024x600")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hcmut.png")), size=(40, 40))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image2.png")), size=(150, 67))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.on=customtkinter.CTkImage(Image.open(os.path.join(image_path, "on2.png")))
        self.off=customtkinter.CTkImage(Image.open(os.path.join(image_path, "off2.png")))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Smart Agriculture", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # cau hinh so cot
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(2, weight=1)
        
        self.is_on = [False, False, False, False, False, False, False, False]
        self.on_button = []
        for i in range(0, self.numberButton):
            self.on_button.append(customtkinter.CTkButton(self.home_frame))

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=1, padx=0, pady=10)

        # Tao cac buton
        self.on_button[0] = customtkinter.CTkButton(self.home_frame, text="Relay 1", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(1))
        self.on_button[0].grid(row=6, column=0, padx=50, pady=15)

        self.on_button[1] = customtkinter.CTkButton(self.home_frame, text="Relay 2", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(2))
        self.on_button[1].grid(row=6, column=1, padx=0, pady=15)

        self.on_button[2] = customtkinter.CTkButton(self.home_frame, text="Relay 3", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(3))
        self.on_button[2].grid(row=6, column=2, padx=50, pady=15)

        self.on_button[3] = customtkinter.CTkButton(self.home_frame, text="Relay 4", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(4))
        self.on_button[3].grid(row=7, column=0, padx=50, pady=15)

        self.on_button[4] = customtkinter.CTkButton(self.home_frame, text="Relay 5", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(5))
        self.on_button[4].grid(row=7, column=1, padx=0, pady=15)

        self.on_button[5] = customtkinter.CTkButton(self.home_frame, text="Relay 6", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(6))
        self.on_button[5].grid(row=7, column=2, padx=50, pady=15)

        self.on_button[6] = customtkinter.CTkButton(self.home_frame, text="Pump1", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(7))
        self.on_button[6].grid(row=8, column=0, padx=80, pady=15)


        self.on_button[7] = customtkinter.CTkButton(self.home_frame, text="Pump2", image=self.on, compound="right", width=150, height=50,
                                                 command=lambda :self.toggle_button_click(8))
        self.on_button[7].grid(row=8, column=2, padx=80, pady=15)

        # Hien thi muc nuoc
        self.distance1 = customtkinter.CTkProgressBar(self.home_frame, orientation="vertical", corner_radius=0, width = 85)
        self.distance1.grid(row = 4, column=0)
        self.lableDistance1= customtkinter.CTkLabel(self.home_frame, text= "Volume of liquid 1", fg_color= "transparent")
        self.lableDistance1.grid(row=5, column= 0, pady=0)

        self.distance2 = customtkinter.CTkProgressBar(self.home_frame, orientation="vertical", corner_radius=0, width = 85)
        self.distance2.grid(row = 4, column=2 )
        self.lableDistance2= customtkinter.CTkLabel(self.home_frame, text= "Volume of liquid 2", fg_color= "transparent", )
        self.lableDistance2.grid(row=5, column= 2, pady=0)

        


#------------------------------------attribute in frame 2------------------------------------------------------
        
        self.image_display_camera_1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_display_camera_1.png")), size=(26, 26))
        
        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_rowconfigure(1, weight=1)

        self.second_frame_top = customtkinter.CTkFrame(self.second_frame, corner_radius=0, fg_color="transparent")
        self.second_frame_bot = customtkinter.CTkFrame(self.second_frame, corner_radius=0, fg_color="transparent")
        self.second_frame_top.grid(row=0)
        self.second_frame_top.grid_columnconfigure(4, weight=1)
        self.second_frame_bot.grid(row=1)
        self.second_frame_bot.grid_columnconfigure(0, weight=1)
        # self.second_frame_bot.grid_rowconfigure(0, weight=1)


        self.lable_display_camera_1 = customtkinter.CTkLabel(self.second_frame_top, text="IP camera 1 :", 
                                                             image= self.image_display_camera_1,
                                                             compound="left", height=20)
        self.lable_display_camera_1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.var_IP_camera_1 = customtkinter.StringVar(value="")
        self.entry_IP_camera_1 = customtkinter.CTkEntry(self.second_frame_top, textvariable=self.var_IP_camera_1, 
                                                        width= 150)
        self.entry_IP_camera_1.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.lable_port_1 = customtkinter.CTkLabel(self.second_frame_top, text="Port Camera 1 :")
        self.lable_port_1.grid(row=0, column= 2, padx=20, pady=10, sticky="w")
        self.port_camera_1 = customtkinter.StringVar(value="4747")
        self.entry_port_1 = customtkinter.CTkEntry(self.second_frame_top, textvariable=self.port_camera_1, 
                                                   width= 50)
        self.entry_port_1.grid(row=0, column= 3, sticky="w")



        self.lable_display_camera_2 = customtkinter.CTkLabel(self.second_frame_top, text="IP camera 2 :", 
                                                             image= self.image_display_camera_1,
                                                             compound="left", height=20)
        self.lable_display_camera_2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.var_IP_camera_2 = customtkinter.StringVar(value="")
        self.entry_IP_camera_2 = customtkinter.CTkEntry(self.second_frame_top, textvariable=self.var_IP_camera_2, 
                                                        width= 150)
        self.entry_IP_camera_2.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.lable_port_2 = customtkinter.CTkLabel(self.second_frame_top, text="Port Camera 2 :")
        self.lable_port_2.grid(row=1, column= 2, padx=20, pady=10, sticky="w")
        self.port_camera_2 = customtkinter.StringVar(value="4747")
        self.entry_port_2 = customtkinter.CTkEntry(self.second_frame_top, textvariable=self.port_camera_2, 
                                                   width= 50)
        self.entry_port_2.grid(row=1, column= 3, sticky="w")
        


        # self.lable_show_camera = customtkinter.CTkLabel(self.second_frame_top, text="Show", width= 100, justify="center")
        # self.lable_show_camera.grid(row=0, column= 4)

        self.camera_all = {'camera 1':self.entry_IP_camera_1.get(),
                           'camera 2':self.entry_IP_camera_2.get()}
        
        self.option_camera = customtkinter.CTkOptionMenu(self.second_frame_top, values=["camera 1","camera 2"], anchor="w",
                                                         command=self.option_display)
        self.option_camera.grid(row=0, column=4, padx=60, sticky="e")

        self.run_button = customtkinter.CTkButton(self.second_frame_top, text="Run", fg_color="green",
                                                  command=self.display_camera)
        self.run_button.grid(row=1, column=4, padx=60, sticky="e")


        self.displayCamera_canvas = customtkinter.CTkCanvas(self.second_frame_bot, height=500, width=1000)
        self.displayCamera_canvas.grid(row=0,column=0, padx=30, pady=30, sticky="nsew")
    
        self.ip = self.var_IP_camera_1.get()
        self.port = self.port_camera_1.get()

#------------------------------------------------------------------------------------------------------------
        
        
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")


#---------------------------------
    def display_camera(self):
        if not self.ip or not self.port:
            print("Please enter valid IP and port")
            return

        self.exit_flag = False  

        url = f"http://{self.ip}:{self.port}/video"

        try:
            cap = cv2.VideoCapture(url)
            if not cap.isOpened():
                print("Failed to open video stream")
                return

            def update_canvas():
                while not self.exit_flag:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_pil = Image.fromarray(frame_rgb)
                    rotated_frame = ImageOps.exif_transpose(frame_pil)
                    photo = ImageTk.PhotoImage(rotated_frame)
                    self.displayCamera_canvas.create_image(0, 0, anchor="nw", image=photo)
                    self.displayCamera_canvas.photo = photo  

                cap.release()
                cv2.destroyAllWindows()

            self.exit_button = customtkinter.CTkButton(self.second_frame_bot, text="Exit", command=self.exit_camera_display)
            self.exit_button.grid(row=1, column=0, padx=10, pady=10, sticky="se")

            self.display_camera_thread = threading.Thread(target=update_canvas)
            self.display_camera_thread.daemon = True
            self.display_camera_thread.start()

        except requests.exceptions.InvalidURL as e:
            print(f"Error: {e}")


    def exit_camera_display(self):
        self.exit_flag = True
        if hasattr(self, "exit_button"):
            self.exit_button.destroy()


    def option_display(self, selected_camera):
        if selected_camera == "camera 1":
            self.ip = self.var_IP_camera_1.get()  
            self.port = self.port_camera_1.get()  
        else:
            self.ip = self.var_IP_camera_2.get()  
            self.port = self.port_camera_2.get()   

#--------------------------------------------------------------------------------------------------------




        
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

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
            #self.control_relay(number, 0)
        else:
            self.UI_Set_Button_text(number, self.on)
            self.is_on[number - 1] = True
            #self.control_relay(number, 1)

    def UI_Set_Button_text(self, number, data):
        if number == 1:
            self.on_button[0].configure(image= data)
        elif number == 2:
            self.on_button[1].configure(image= data)
        elif number == 3:
            self.on_button[2].configure(image= data)
        elif number == 4:
            self.on_button[3].configure(image= data)
        elif number == 5:
            self.on_button[4].configure(image= data)
        elif number == 6:
            self.on_button[5].configure(image= data)
        elif number == 7:
            self.on_button[6].configure(image= data)
        elif number == 8:
            self.on_button[7].configure(image= data)
    
    def UI_Set_Value_Text(self, text_object, data):
        text_object.configure(text="%.2f" %data)

    def UI_Refresh(self):
        #self.slider_Refresh(self.distance1, self.dataModel.getvalueDistance(9))
        #self.slider_Refresh(self.distance2, self.dataModel.getvalueDistance(12))
        self.update()

    #update muc nuoc, chieu cao cua thung la 3000 mm
    def slider_Refresh(self, object, value):
        object.set(1 - (value/3000))
        
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

app=App(None)
while(True): 
    app.UI_Refresh()
    time.sleep(0.1)
        
        

    
