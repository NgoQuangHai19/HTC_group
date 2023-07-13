import tkinter as tk
from RS485Controller import RS485Controller

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
    value_text.delete(1.0, tk.END)
    value_text.insert(tk.END, distance)

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Control Panel")
root.geometry("400x300")
root.attributes("-fullscreen", True)  # Thiết lập cửa sổ thành chế độ toàn màn hình

# Nút điều khiển relay 1-3
relay_frame1 = tk.Frame(root)
relay_frame1.pack(pady=10)

for i in range(3):
    relay_frame = tk.Frame(relay_frame1)
    relay_frame.pack(side=tk.LEFT, padx=5)

    relay_label = tk.Label(relay_frame, text="Relay {}".format(i+1))
    relay_label.pack()

    on_button = tk.Button(relay_frame, text="ON", width=5, command=lambda num=i+1: control_relay(num, 1))
    on_button.pack(pady=5)

    off_button = tk.Button(relay_frame, text="OFF", width=5, command=lambda num=i+1: control_relay(num, 0))
    off_button.pack(pady=5)

# Nút điều khiển relay 4-6
relay_frame2 = tk.Frame(root)
relay_frame2.pack(pady=10)

for i in range(3, 6):
    relay_frame = tk.Frame(relay_frame2)
    relay_frame.pack(side=tk.LEFT, padx=5)

    relay_label = tk.Label(relay_frame, text="Relay {}".format(i+1))
    relay_label.pack()

    on_button = tk.Button(relay_frame, text="ON", width=5, command=lambda num=i+1: control_relay(num, 1))
    on_button.pack(pady=5)

    off_button = tk.Button(relay_frame, text="OFF", width=5, command=lambda num=i+1: control_relay(num, 0))
    off_button.pack(pady=5)

# Nút điều khiển relay 7, 8, 10, 11
relay_frame3 = tk.Frame(root)
relay_frame3.pack(pady=10)

for i in [7, 8, 10, 11]:
    relay_frame = tk.Frame(relay_frame3)
    relay_frame.pack(side=tk.LEFT, padx=5)

    relay_label = tk.Label(relay_frame, text="Relay {}".format(i))
    relay_label.pack()

    on_button = tk.Button(relay_frame, text="ON", width=5, command=lambda num=i: control_relay(num, 1))
    on_button.pack(pady=5)

    off_button = tk.Button(relay_frame, text="OFF", width=5, command=lambda num=i: control_relay(num, 0))
    off_button.pack(pady=5)

# Nút điều khiển relay 9, 12
relay_frame4 = tk.Frame(root)
relay_frame4.pack(pady=10)

relay_frame_9 = tk.Frame(relay_frame4)
relay_frame_9.pack(side=tk.LEFT, padx=5)

relay_label_9 = tk.Label(relay_frame_9, text="Relay 9")
relay_label_9.pack()

measure_button_9 = tk.Button(relay_frame_9, text="Measure", width=10, command=lambda: measure_distance(9))
measure_button_9.pack(pady=5)

value_frame = tk.Frame(relay_frame4)
value_frame.pack(side=tk.LEFT, padx=5)

value_label = tk.Label(value_frame, text="Value:")
value_label.pack(side=tk.LEFT)

value_text = tk.Text(value_frame, width=10, height=1)
value_text.pack(side=tk.LEFT)

relay_frame_12 = tk.Frame(relay_frame4)
relay_frame_12.pack(side=tk.LEFT, padx=5)

relay_label_12 = tk.Label(relay_frame_12, text="Relay 12")
relay_label_12.pack()

measure_button_12 = tk.Button(relay_frame_12, text="Measure", width=10, command=lambda: measure_distance(12))
measure_button_12.pack(pady=5)

root.mainloop()
