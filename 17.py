def sort_array(arr):
    return sorted(arr)# in the array we have sorted function that make array in acsnding array;

#we use split  for enter the  by spater input by space 
input_list = input("Enter elements of the array separated by spaces: ").split()
input_array = [int(num) for num in input_list]# we make array of input by for loop by using num intger


sorted_array = sort_array(input_array)#this our variable that store function 
print("Sorted array in ascending order:", sorted_array)
