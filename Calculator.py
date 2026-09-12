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
    bg="#1F1F1F",
    fg='white',
    bd=0
)

display.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=0,
    pady=5,
    ipady=15
)

def button_clicks(value):
    if value == "Del":
        display.delete(len(display.get()) - 1, tk.END)

    elif value == "C":
        display.delete(0, tk.END)

    elif value in ("X", "-", "/", "+"):
        current = display.get()

        if current == "":
            return

        if current[-1] in ("*", "-", "/", "+"):
            return

        if value == "X":
            display.insert(tk.END, "*")
        else:
            display.insert(tk.END, value)

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
    
    ("()", 5, 0),
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
