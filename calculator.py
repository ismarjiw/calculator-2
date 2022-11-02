"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
    input_string = input('Enter your equation: ')
    tokens = input_string.split(' ') 
    total = None 

    if len(tokens) == 1 and 'q' in tokens:
        break 

    num1 = float(tokens[1])
    num2 = float(tokens[2])

    if len(tokens) == 3: 
        if tokens[0] == '+':
            total = add(num1, num2)
        elif tokens[0] == '-':
            total = subtract(num1, num2)
        elif tokens[0] == '*':
            total = multiply(num1, num2)
        elif tokens[0] == '/':
            total = divide(num1, num2)
        elif tokens[0] == 'square':
            total = square(num1, num1)
        elif tokens[0] == 'cube':
            total = cube(num1, num1)
        elif tokens[0] == 'mod':
            total = mod(num1, num2)
        elif tokens[0] == 'pow':
            total = power(num1, num2)
                
    print(total)












