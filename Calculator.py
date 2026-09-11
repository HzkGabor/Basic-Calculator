import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry('505x620')
window.resizable(False, False)
window.config(bg='#0f0f0f')

display = tk.Entry(
    window,
    font=('Arial', 32),
    justify='right',
    bg="#222222",
    fg='white'
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=20,
    ipady=15
)

def button_clicks(value):
    if value == "Del":
        display.delete(len(display.get()) - 1, tk.END)

    elif value == "C":
        display.delete(0, tk.END)

    elif value == "x":
        display.insert(tk.END, "*")

    elif value == '-':
        display.insert(tk.END, '-')

    elif value == '/':
        display.insert(tk.END, '/')

    elif value == '+':
            display.insert(tk.END, '+')

    elif value == "=":
        expression = display.get()

        try:
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, result)

        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    else:
        display.insert(tk.END, value)

buttons = [
    ("C", 1, 0),
    ("Del", 1, 1),
    ("%", 1, 2),
    ("/", 1, 3),
    
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("x", 2, 3),
    
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("-", 3, 3),
    
    ("7", 4, 0),
    ("8", 4, 1),
    ("9", 4, 2),
    ("+", 4, 3),
    
    ("()", 5, 0),
    ("0", 5, 1),
    (".", 5, 2),
    ("=", 5, 3),
]

for text, row, column in buttons:

    button = tk.Button(
        window,
        text=text,
        font=("Arial", 20),
        width=6,
        height=2,

        bg="#333333",
        fg="white",
        activebackground="#555555",
        activeforeground="white",

        command=lambda value=text: button_clicks(value)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

window.mainloop()
