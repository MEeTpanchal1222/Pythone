def remove_duplicates(arr):
    return list(set(arr))# set function that 

# User input for the array
input_list = input("Enter elements of the array separated by spaces: ").split()
input_array = [int(num) for num in input_list]

# Removing duplicates
cleaned_array = remove_duplicates(input_array)
print("Array after removing duplicates:", cleaned_array)
