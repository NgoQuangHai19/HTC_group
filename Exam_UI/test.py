import customtkinter
import os
from PIL import Image
import time
import cv2
import numpy as np
import requests

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

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, 
                                                             text="  Smart Agriculture", 
                                                             image=self.logo_image,
                                                             compound="left", 
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, 
                                                   corner_radius=0, height=40, 
                                                   border_spacing=10, text="Home",
                                                   fg_color="transparent", 
                                                   text_color=("gray10", "gray90"), 
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, 
                                                   anchor="w", 
                                                   command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, 
                                                      corner_radius=0, height=40, 
                                                      border_spacing=10, text="Frame 2",
                                                      fg_color="transparent", 
                                                      text_color=("gray10", "gray90"), 
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, 
                                                      anchor="w", 
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, 
                                                      corner_radius=0, 
                                                      height=40, 
                                                      border_spacing=10, 
                                                      text="Frame 3",
                                                      fg_color="transparent", 
                                                      text_color=("gray10", "gray90"), 
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", 
                                                      command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, 
                                                                values=["Light", "Dark", "System"],
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
        self.distance1 = customtkinter.CTkProgressBar(self.home_frame, orientation="vertical", corner_radius=5, width = 85)
        self.distance1.grid(row = 4, column=0)
        self.lableDistance1= customtkinter.CTkLabel(self.home_frame, text= "Volume of liquid 1", fg_color= "transparent")
        self.lableDistance1.grid(row=5, column= 0, pady=0)

        self.distance2 = customtkinter.CTkProgressBar(self.home_frame, orientation="vertical", corner_radius=5, width = 85)
        self.distance2.grid(row = 4, column=2 )
        self.lableDistance2= customtkinter.CTkLabel(self.home_frame, text= "Volume of liquid 2", fg_color= "transparent", )
        self.lableDistance2.grid(row=5, column= 2, pady=0)

        

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    #--------------------------------------------------------------------------------------------------
    # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create chat box
        self.chat_box = customtkinter.CTkTextbox(self.second_frame, width=80, height=10)
        self.chat_box.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        # create switch button
        self.switch_state = False
        self.switch_image_on = customtkinter.CTkImage(Image.open(os.path.join(image_path, "switch_on.png")), size=(100, 40))
        self.switch_image_off = customtkinter.CTkImage(Image.open(os.path.join(image_path, "switch_off.png")), size=(100, 40))
        self.switch_button = customtkinter.CTkButton(self.second_frame,
                                                     text="Switch",
                                                     image=self.switch_image_off,
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=12),
                                                     command=self.toggle_switch)
        self.switch_button.grid(row=1, column=0, padx=20, pady=20)

        # create camera label
        self.camera_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "hcmut.png")), size=(640, 360))
        self.camera_label = customtkinter.CTkLabel(self.second_frame, image=self.camera_image)
        self.camera_label.grid(row=2, column=0, padx=20, pady=20)

        # set the current camera index
        self.current_camera = 1

        # select default frame
        self.select_frame_by_name("home")

    # ... (previous code)

    def toggle_switch(self):
        self.switch_state = not self.switch_state
        if self.switch_state:
            self.switch_button.configure(image=self.switch_image_on)
        else:
            self.switch_button.configure(image=self.switch_image_off)

        # switch between Camera 1 and Camera 2
        if self.current_camera == 1:
            self.current_camera = 2
        else:
            self.current_camera = 1

        # Display camera based on the current camera index
        self.display_camera()

    def display_camera(self):
    # set the IP and port of the selected camera
        if self.current_camera == 1:
            ip = "192.168.1.86"
        else:
            ip = "10.128.91.182"
        port = 4747

        # Tạo URL để truy cập video từ camera
        url = "http://" + ip + ":" + str(port) + "/video"

        # Mở kết nối đến camera thông qua URL
        stream = requests.get(url, stream=True)

        # Đọc dữ liệu video từ camera
        bytes_data = bytes()
        for chunk in stream.iter_content(chunk_size=1024):
            bytes_data += chunk
            a = bytes_data.find(b'\xff\xd8')
            b = bytes_data.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytes_data[a:b+2]
                bytes_data = bytes_data[b+2:]
                # Hiển thị video từ dữ liệu nhận được
                frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                frame = cv2.resize(frame, (640, 360))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                self.camera_image.set_image(image)
                self.camera_label.update()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Đóng kết nối và giải phóng tài nguyên
        stream.close()
        cv2.destroyAllWindows()

    #------------------------------------------------------------------------------------------------


        
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
        self.slider_Refresh(self.distance1, self.dataModel.getvalueDistance(9))
        self.slider_Refresh(self.distance2, self.dataModel.getvalueDistance(12))
        self.home_frame.update()

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
    

if __name__ == "__main__":
    app = App(None)
    app.mainloop()
    time.sleep(1)
        
        

    

