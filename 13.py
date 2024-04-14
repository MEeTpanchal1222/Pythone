def is_palindrome(string):
    # Convert the string to lowercase 
    string = string.lower()
    
    string = ''.join(char for char in string if char.isalnum())
    #''.join(...): This constructs a new string. 
    #char.isalnum(): Alphanumeric means the character is either a letter (a-z, A-Z) or a digit (0-9).
    return string == string[::-1]


input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
