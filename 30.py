def square_root(number, precision=0.0001):
   
    guess = number / 2
    while abs(guess * guess - number) > precision:
        guess = (guess + number / guess) / 2
    return guess


number = float(input("Enter a number to find its square root: "))
result = square_root(number)
print("The square root of", number, "is approximately:", result)
