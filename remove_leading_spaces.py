# Program: Remove leading spaces without using lstrip()

# Get input from the user
user_input = input("Enter a string: ")

# Initialize index to track the first non-space character
index = 0

# Loop until a non-space character is found
while index < len(user_input) and user_input[index] == " ":
    index += 1

# Extract the substring starting from the first non-space character
result = user_input[index:]

# Display the result
print(result)