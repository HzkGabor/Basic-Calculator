print('=========================')
print('Welcome to my Calculator!')
print('=========================')


num1 = int(input('Your first number? '))
num2 = int(input('Your second number? '))
userinput = input('Your mathematical operation? ')
# This is where we get the information to use!
def calculate():
    if userinput == 'Plus':
        print(num1 + num2)
    elif userinput == 'Minus':
        print(num1 - num2)
    elif userinput == 'Multiply':
        print(num1 * num2)
    elif userinput == 'Divide':
        print(num1 / num2)
    else:
        print('Something Went Wrong!')

# Here I have made the Functions for my calculator!

calculate()

# Here I have called the Function!