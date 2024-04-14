def sum_of_digits(n):
    
    if n < 10:
        return n
    
    else:
        return n % 10 + sum_of_digits(n // 10)


number = int(input("Enter a number to find the sum of its digits: "))
result = sum_of_digits(number)
print("The sum of digits of", number, "is:", result)
