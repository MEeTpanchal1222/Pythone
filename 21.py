def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator(operation, x, y):
    operations_dict = { # just like map key nad value 
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    # WE using key by if
    if operation in operations_dict:
        
        func = operations_dict[operation]
        
        result = func(x, y)
        return result
    else:
        return "Invalid operation"


operation = input("Enter operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator(operation, num1, num2)
print("Result:", result)
