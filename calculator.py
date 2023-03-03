import tkinter as tk
from tkinter import ttk
import pypresence

# Define functions for operations
def add(): # define +
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 + num2
    label_result.config(text="Result: " + str(result))
    update_rpc()

def subtract(): # define -
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label_result.config(text="Result: " + str(result))
    update_rpc

def multiply(): # define *
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label_result.config(text="Result: " + str(result))
    update_rpc

def divide(): # define /
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 / num2
    label_result.config(text="Result: " + str(result))
    update_rpc

def update_rpc(): # update Discord Rich Presence
    rpc.update(state="Calculating...", details="Performing a calculation", large_image="calculator", large_text="Calculator by CXA0Luvx")

# Create tkinter window
root = tk.Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
root.config(bg="#1C1C1C")

# Create entry boxes and labels
label1 = tk.Label(root, text="First number:", font=("Arial", 14), fg="#FFFFFF", bg="#1C1C1C")
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = ttk.Entry(root, font=("Arial", 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Second number:", font=("Arial", 14), fg="#FFFFFF", bg="#1C1C1C")
label2.grid(row=1, column=0, padx=10, pady=10)

entry2 = ttk.Entry(root, font=("Arial", 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create buttons for operations
button_add = ttk.Button(root, text="Add", style="TButton", command=add)
button_add.grid(row=2, column=0, padx=10, pady=10)

button_subtract = ttk.Button(root, text="Subtract", style="TButton", command=subtract)
button_subtract.grid(row=2, column=1, padx=10, pady=10)

button_multiply = ttk.Button(root, text="Multiply", style="TButton", command=multiply)
button_multiply.grid(row=3, column=0, padx=10, pady=10)

button_divide = ttk.Button(root, text="Divide", style="TButton", command=divide)
button_divide.grid(row=3, column=1, padx=10, pady=10)

# Create label for result
label_result = tk.Label(root, text="Result: ", font=("Arial", 14), fg="#FFFFFF", bg="#1C1C1C")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Define ttk styles for buttons
style = ttk.Style()
style.configure("TButton", background="#4CAF50", foreground="#1C1C1C")

# Set up Discord RPC
client_id = 'put client id here'
rpc = pypresence.Presence(client_id=client_id)
rpc.connect()

update_rpc() # initial update

root.mainloop()
