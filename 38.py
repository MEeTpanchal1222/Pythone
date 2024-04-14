def safe_divide(dividend, divisor):
    try:
        result = dividend / divisor
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    return result

# Test the function
dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))

result = safe_divide(dividend, divisor)
if result is not None:
    print("Result of the division:", result)
