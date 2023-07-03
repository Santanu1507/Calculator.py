import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=25, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row, col = 1, 0
for button in buttons:
    if col == 4:
        col = 0
        row += 1

    btn = tk.Button(root, text=button, width=6, height=3,
                    command=lambda btn=button: button_click(btn))
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1

clear_button = tk.Button(root, text="C", width=5, height=2, command=button_clear)
clear_button.grid(row=row, column=col, padx=5, pady=5)

equal_button = tk.Button(root, text="=", width=5, height=2, command=button_equal)
equal_button.grid(row=row+1, column=col, padx=5, pady=5)

root.mainloop()
