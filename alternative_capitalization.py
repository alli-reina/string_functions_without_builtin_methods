# Program: Manually Capitalize First Letter of a String

input_string = input("Enter a string: ")

if not input_string:
    print("Empty string.")
else:
    first_letter = input_string[0].upper()
    remaining_letters = input_string[1:].lower()
    print(first_letter + remaining_letters)