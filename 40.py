def handle_index_error(arr, index):
    try:
        value = arr[index]
        print("Value at index", index, ":", value)
    except IndexError:
        print("Error: Index out of range.")


arr = [1, 2, 3, 4, 5]
index = int(input("Enter the index to access: "))

handle_index_error(arr, index)
