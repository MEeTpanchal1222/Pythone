M=1
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    M= 1  
    for k in range(1,i+1):
        print(' ', M, sep='', end='')
        M = M * (i - k) // k
    print()