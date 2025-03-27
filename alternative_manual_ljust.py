# Program: Manual Implementation of ljust()

# Get input from the user
input_string = input("Enter a string: ")

# Get the desired width from the user
width = int(input("Enter the desired width: "))

# Check if the string length is less than the desired width
if len(input_string) < width:
    # Calculate how many spaces to add
    spaces_to_add = width - len(input_string)

# Step 5: Append the spaces to the right of the string
# Step 6: Print the result