def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError: 
        print("Error: File not found.")

# Test the function
filename = input("Enter the name of the file to read: ")
read_file(filename)
