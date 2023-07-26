import tkinter as tk

def on_button_click():
    # Add your action here when the button is clicked
    print("Button clicked!")

def on_submit():
    # Add your action here when the submit button is clicked
    input_text = entry.get()
    print(f"Submitted: {input_text}")

# Create the main application window
root = tk.Tk()
root.title("Dashboard")

# Create and place widgets in the window
label1 = tk.Label(root, text="Welcome to the Dashboard!", font=("Arial", 16))
label1.pack(pady=20)

button1 = tk.Button(root, text="Click Me!", command=on_button_click, width=20)
button1.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit, width=20)
submit_button.pack(pady=10)

label2 = tk.Label(root, text="Status:", font=("Arial", 12))
label2.pack(pady=10)

status_label = tk.Label(root, text="Waiting for input...", font=("Arial", 12))
status_label.pack(pady=10)

# Start the main event loop
root.mainloop()
