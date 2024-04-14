def is_prime(n):
    if n <= 1:# for check number is smaller then  1
        return False
    elif n <= 3:# for check nuber is smaller then 3 
        return True #true for 3 and 2 is  prime numer 
    elif n % 2 == 0 or n % 3 == 0:#FOR that number who by divde 2,3
        return False
    i = 5
    while i * i <= n  : # for number is beggier then 25
        if n % i == 0 or n % 7 == 0: return False  
    return True


num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
