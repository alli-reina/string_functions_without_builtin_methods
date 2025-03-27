# Program: Remove a prefix manually without using removeprefix()

# Ask the user to enter a string
input_string = input("Enter a string: ")

# Ask the user to enter a prefix to remove
prefix = input("Enter a prefix to remove: ")

# Check if the string starts with the given prefix
if input_string.startswith(prefix):
    # Remove the prefix by slicing
    result_string = input_string[len(prefix):]
else:
    # Keep the string unchanged
    result_string = input_string

# Step 6: Display the result