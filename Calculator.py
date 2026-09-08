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
