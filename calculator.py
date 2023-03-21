import tkinter as tk
from tkinter import ttk

def calculate(operator):
    try:
        num1, num2 = float(entry1.get()), float(entry2.get())
        result = {
            '+': num1 + num2,
            '-': num1 - num2,
            '*': num1 * num2,
            '/': num1 / num2
        }[operator]
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input")

root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)
root.config(bg="#1C1C1C")

label1 = tk.Label(root, text="First number:", font=("Arial", 14), fg="#FFFFFF", bg="#1C1C1C")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = ttk.Entry(root, font=("Arial", 14))
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Second number:", font=("Arial", 14), fg="#FFFFFF", bg="#1C1C1C")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = ttk.Entry(root, font=("Arial", 14))
entry2.grid(row=1, column=1, padx=10, pady=10)

ttk.Button(root, text="+", style="TButton", command=lambda: calculate('+')).grid(row=2, column=0, padx=10, pady=10)
ttk.Button(root, text="-", style="TButton", command=lambda: calculate('-')).grid(row=2, column=1, padx=10, pady=10)
ttk.Button(root, text="*", style="TButton", command=lambda: calculate('*')).grid(row=3, column=0, padx=10, pady=10)
ttk.Button(root, text="/", style="TButton", command=lambda: calculate('/')).grid(row=3, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 14), fg="#FFFFFF", bg="#1C1C1C")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

style = ttk.Style()
style.configure("TButton", background="#4CAF50", foreground="#1C1C1C")

root.mainloop()
