def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def print_prime_numbers(start, end):
    print("Prime numbers between", start, "and", end, "are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")



start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

print_prime_numbers(start_num, end_num)
