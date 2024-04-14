def intersection_of_arrays(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1.intersection(set2))


input_list1 = input("Enter elements of the first array separated by spaces: ").split()
input_list2 = input("Enter elements of the second array separated by spaces: ").split()


array1 = [int(num) for num in input_list1]
array2 = [int(num) for num in input_list2]

result = intersection_of_arrays(array1, array2)
print("The intersection of the arrays is:", result)
