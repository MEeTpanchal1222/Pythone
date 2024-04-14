def count_character_occurrences(input_string, character):
    return input_string.count(character)# we have count function  by string elemnts


input_string = input("Enter a string: ")#string input
character = input("Enter the character to count: ")#that charcter in string so we cout in string

#check character length is only one;
if len(character) != 1:
    print("Please enter exactly one character.")
else:
    count = count_character_occurrences(input_string, character)
    print(f"The character '{character}' appears {count} times in the string.")
