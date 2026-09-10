import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry('505x630')
window.resizable(False, False)
window.config(bg='#0f0f0f')

display = tk.Entry(
    window,
    font=('Arial', 32),
    justify='right',
    bg="#222222"
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
    print(value) 

buttons = [
    ("C", 1, 0),
    ("del", 1, 1),
    ("%", 1, 2),
    ("÷", 1, 3),
    
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("×", 2, 3),
    
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("−", 3, 3),
    
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
        width=5,
        height=2,

        bg="#333333",
        fg="white",
        activebackground="#555555",
        activeforeground="white",

        command=lambda value=text: button_click(value)
    )

    button.grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )

window.mainloop()

num1 = int(input('What is your first number? '))
num2 = int(input('What is your second number? '))
operation = input('What is your operation (+, -, *, /)? ')

def calculation(num1, operation, num2):
    if operation in('+'):
        return num1 + num2
    elif operation in('-'):
        return num1 - num2
    elif operation in('*'):
        return num1 * num2
    elif operation in('/'):
        if num2 == 0:
            print('You cant divide by zero!')
            return num1
        return num1 / num2
        
    else:
        print('Something Went Wrong!')
        return num1

result = calculation(num1, operation, num2)
print('Result:', result)

while True:
    choise = input('Do you want to continue (Yes or No)? ')

    if choise != 'Yes':
        print('Goodbye!')
        break
    else:
        next_operation = input('What is your operation (+, -, *, /)? ')
        next_num = int(input('What is your next number? '))

        result = calculation(result, next_operation, next_num)
        print('New Result:', result)
