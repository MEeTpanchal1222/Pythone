def calculate_average(arr):
    if len(arr) == 0:
        return 0  
    return sum(arr) / len(arr)

# Test the function
arr = [10, 20, 30, 40, 50]
average = calculate_average(arr)
print("The average of elements in the array is:", average)
