def reverse_number(number):
    reversed_number = 0
    while number > 0:                                           
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
    return reversed_number


num = int(input("Enter a number to reverse: "))
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)
