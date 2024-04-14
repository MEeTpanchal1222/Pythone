def sum_of_natural_numbers(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1#go to zero
    return sum

number = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(number)
print("The sum of natural numbers up to", number, "is:", result)
