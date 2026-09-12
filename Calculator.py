import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry('480x370')
window.resizable(False, False)
window.config(bg='#0f0f0f')

display = tk.Entry(
    window,
    font=('Arial', 32, 'bold'),
    justify='right',
    bg="#1B1B1B",
    fg='black',
    bd=0,
    state='readonly'
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=0,
    pady=5,
    ipady=15
)

def display_insert(value):
    display.config(state='normal')
    display.insert(tk.END, value)
    display.config(state='readonly')

def display_delete(start, end=None):
    display.config(state='normal')

    if end is None:
        display.delete(start)
    else:
        display.delete(start, end)

    display.config(state='readonly')

def button_clicks(value):
    if value == "Del":
        current = display.get()

        if current == "Error":
            display_delete(0, tk.END)

        elif current:
            display_delete(len(current) - 1, tk.END)

    elif value == "C":
        display_delete(0, tk.END)

    elif value == "%":
        current = display.get()

        if current == "":
            return

        try:
            result = float(current) / 100

            if result.is_integer():
                result = int(result)

            display_delete(0, tk.END)
            display_insert(result)

        except:
            display_delete(0, tk.END)
            display_insert("Error")

    elif value in ("X", "-", "/", "+"):
        current = display.get()

        if current == "":
            return

        if current[-1] in ("*", "-", "/", "+"):
            return

        if value == "X":
            display_insert("*")
        else:
            display_insert(value)

    elif value == "=":
        expression = display.get()

        try:
            result = eval(expression)

            display_delete(0, tk.END)
            display_insert(result)

        except:
            display_delete(0, tk.END)
            display_insert("Error")

    else:
        display_insert(value)

buttons = [
    ("C", 1, 0),
    ("Del", 1, 1),
    ("%", 1, 2),
    ("()", 1, 3),

    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    ("X", 2, 3),

    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("-", 3, 3),

    ("1", 4, 0),
    ("2", 4, 1),
    ("3", 4, 2),
    ("+", 4, 3),

    ("/", 5, 0),
    ("0", 5, 1),
    (".", 5, 2),
    ("=", 5, 3),
]

for text, row, column in buttons:

    button = tk.Button(
        window,
        text=text,
        font=("Arial", 20, 'bold'),
        width=5,
        height=1,

        bg="#3D3D3D",
        fg="white",
        bd=0,
        activebackground="#060549",
        activeforeground="white",

        command=lambda value=text: button_clicks(value)
    )

    button.grid(
        row=row,
        column=column,
        sticky='nsew',
        padx=1,
        pady=1
    )

window.mainloop()
