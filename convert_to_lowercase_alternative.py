# Program: Convert all uppercase letters to lowercase without using lower()

# Get input from the user
input_string = input("Enter a string: ")

# Step 2: Create an empty string for the result
result = ""

# Go through each letter in the input
for letter in input_string:
    # If it's uppercase, convert to lowercase
    if "A" <= letter <= "Z":
        letter = chr(ord(letter) + 32)

    # Add it to the result
    result += letter

# Print the final result
print("Final string:", result)