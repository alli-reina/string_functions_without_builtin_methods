# Program: Manually Capitalize First Letter of a String

# Get input from the user
input_string = input("Enter a string: ")

# Check if the string is not empty
if input_string:
    # Convert the first letter to uppercase
    first_letter = input_string[0].upper().

# Convert the rest of the string to lowercase
    remaining_letters = input_string[1:].lower()

    # Combine and print the result
    print(first_letter + remaining_letters)
else:
    print("Empty string.")