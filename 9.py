def fibonacci(n): #for function 
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])#now add in array  F(n)=F(n−1)+F(n−2) by this formula 
    return fib_series
#function is over now 


#input number 
num_terms = int(input("Enter the number of terms for Fibonacci series: "))
fib_series = fibonacci(num_terms)#function call and store in variabile for printing
print("Fibonacci series up to", num_terms, "terms:", fib_series)#print all serise 
