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

# Tạo giao diện người dùng
root = tk.Tk()
root.title("Control Panel")
root.geometry("400x300")

# Nút điều khiển relay 1-6
relay_frame = tk.Frame(root)
relay_frame.pack(pady=10)

for i in range(6):
    button_frame = tk.Frame(relay_frame)
    button_frame.pack(pady=5)

    label = tk.Label(button_frame, text="Relay {}".format(i+1))
    label.pack()

    on_button = tk.Button(button_frame, text="ON", width=5, command=lambda num=i+1: control_relay(num, 1))
    on_button.pack(side=tk.LEFT, padx=5)

    off_button = tk.Button(button_frame, text="OFF", width=5, command=lambda num=i+1: control_relay(num, 0))
    off_button.pack(side=tk.LEFT)

# Nút điều khiển relay 7, 8, 10, 11
relay_frame2 = tk.Frame(root)
relay_frame2.pack(pady=10)

for i in [7, 8, 10, 11]:
    button_frame = tk.Frame(relay_frame2)
    button_frame.pack(pady=5)

    label = tk.Label(button_frame, text="Relay {}".format(i))
    label.pack()

    on_button = tk.Button(button_frame, text="ON", width=5, command=lambda num=i: control_relay(num, 1))
    on_button.pack(side=tk.LEFT, padx=5)

    off_button = tk.Button(button_frame, text="OFF", width=5, command=lambda num=i: control_relay(num, 0))
    off_button.pack(side=tk.LEFT)

# Nút đo khoảng cách 9, 12
distance_frame = tk.Frame(root)
distance_frame.pack(pady=10)

button_frame = tk.Frame(distance_frame)
button_frame.pack(pady=5)

distance_button_9 = tk.Button(button_frame, text="9", width=5, command=lambda: measure_distance(9))
distance_button_9.pack(side=tk.LEFT, padx=5)

distance_button_12 = tk.Button(button_frame, text="12", width=5, command=lambda: measure_distance(12))
distance_button_12.pack(side=tk.LEFT)

# Hiển thị giá trị trả về của hàm getvalueDistance(number)
value_frame = tk.Frame(root)
value_frame.pack(pady=10)

value_label = tk.Label(value_frame, text="Giá trị trả về")
value_label.pack()

value_text = tk.Text(value_frame, width=20, height=1)
value_text.pack()

def update_value_text(value):
    value_text.delete(1.0, tk.END)
    value_text.insert(tk.END, value)

root.mainloop()
