def power(base, powerofnum):
    result = 1
    for _ in range(powerofnum):
        result *= base
    return result


base = float(input("Enter the base number: "))
powerofnum = int(input("Enter the exponent: "))

result = power(base, powerofnum)
print(base, "raised to the power of", powerofnum, "is:", result)
