import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=16, font=("Times New Roman", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_value = 1
col_value = 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=4, height=2, font=("Arial", 14),
              command=lambda value=button_text: clear_entry() if value == 'C' else on_button_click(value) if value != '=' else calculate())\
        .grid(row=row_value, column=col_value, padx=5, pady=5)
    col_value += 1
    if col_value> 3:
        col_value = 0
        row_value += 1

root.mainloop()
