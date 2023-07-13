import tkinter as tk
from tkinter import ttk
from RS485Controller import RS485Controller
import threading

# Khởi tạo đối tượng RS485Controller
ser = RS485Controller()

# Hàm điều khiển relay
def control_relay(number, state):
    if state == 1:
        ser.relayController(number, 1)
        print("Relay {} is ON".format(number))
    elif state == 0:
        ser.relayController(number, 0)
        print("Relay {} is OFF".format(number))

# Hàm đo khoảng cách
def measure_distance(number):
    distance = ser.getvalueDistance(number)
    print("Khoảng cách nút {}: {}".format(number, distance))
    if number == 9:
        relay_9_value.set(distance)
    elif number == 12:
        relay_12_value.set(distance)

# Hàm cập nhật giá trị của Relay 9 và 12
def update_values():
    while True:
        measure_distance(9)
        measure_distance(12)
        time.sleep(15)

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Control Panel")

# Lấy kích thước của màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Thiết lập kích thước và vị trí cho cửa sổ
window_width = int(screen_width / 2)
window_height = int(screen_height / 2)
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Nút điều khiển relay 1-3
relay_frame1 = ttk.Frame(root)
relay_frame1.pack(pady=10)

for i in range(3):
    relay_frame = ttk.Frame(relay_frame1)
    relay_frame.pack(side=tk.LEFT, padx=10, pady=10)

    relay_label = ttk.Label(relay_frame, text="Relay {}".format(i+1))
    relay_label.pack()

    on_button = ttk.Button(relay_frame, text="ON", width=5, command=lambda num=i+1: control_relay(num, 1))
    on_button.pack(pady=5)

    off_button = ttk.Button(relay_frame, text="OFF", width=5, command=lambda num=i+1: control_relay(num, 0))
    off_button.pack(pady=5)

# Nút điều khiển relay 4-6
relay_frame2 = ttk.Frame(root)
relay_frame2.pack(pady=10)

for i in range(3, 6):
    relay_frame = ttk.Frame(relay_frame2)
    relay_frame.pack(side=tk.LEFT, padx=10, pady=10)

    relay_label = ttk.Label(relay_frame, text="Relay {}".format(i+1))
    relay_label.pack()

    on_button = ttk.Button(relay_frame, text="ON", width=5, command=lambda num=i+1: control_relay(num, 1))
    on_button.pack(pady=5)

    off_button = ttk.Button(relay_frame, text="OFF", width=5, command=lambda num=i+1: control_relay(num, 0))
    off_button.pack(pady=5)

# Nút điều khiển relay 7, 8
relay_frame3 = ttk.Frame(root)
relay_frame3.pack(pady=10)

for i in [7, 8]:
    relay_frame = ttk.Frame(relay_frame3)
    relay_frame.pack(side=tk.LEFT, padx=10, pady=10)

    relay_label = ttk.Label(relay_frame, text="Relay {}".format(i))
    relay_label.pack()

    on_button = ttk.Button(relay_frame, text="ON", width=5, command=lambda num=i: control_relay(num, 1))
    on_button.pack(pady=5)

    off_button = ttk.Button(relay_frame, text="OFF", width=5, command=lambda num=i: control_relay(num, 0))
    off_button.pack(pady=5)

# Nút điều khiển relay 9, 12
relay_frame4 = ttk.Frame(root)
relay_frame4.pack(pady=10)

relay_frame_9 = ttk.Frame(relay_frame4)
relay_frame_9.pack(side=tk.LEFT, padx=10, pady=10)

relay_label_9 = ttk.Label(relay_frame_9, text="Relay 9")
relay_label_9.pack()

measure_button_9 = ttk.Button(relay_frame_9, text="Measure", width=10, command=lambda: measure_distance(9))
measure_button_9.pack(pady=5)

relay_9_value = tk.StringVar()
relay_9_label = ttk.Label(relay_frame_9, textvariable=relay_9_value)
relay_9_label.pack()

relay_frame_12 = ttk.Frame(relay_frame4)
relay_frame_12.pack(side=tk.LEFT, padx=10, pady=10)

relay_label_12 = ttk.Label(relay_frame_12, text="Relay 12")
relay_label_12.pack()

measure_button_12 = ttk.Button(relay_frame_12, text="Measure", width=10, command=lambda: measure_distance(12))
measure_button_12.pack(pady=5)

relay_12_value = tk.StringVar()
relay_12_label = ttk.Label(relay_frame_12, textvariable=relay_12_value)
relay_12_label.pack()

# Tạo luồng riêng để cập nhật giá trị của Relay 9 và 12
update_thread = threading.Thread(target=update_values)
update_thread.daemon = True
update_thread.start()

root.mainloop()
