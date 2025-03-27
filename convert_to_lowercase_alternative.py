# Program: Convert all uppercase letters to lowercase without using lower()

# Get input from the user
input_string = input("Enter a string: ")

# Create an empty result string
result = ""
 
# Go through each letter in the input
for letter in input_string:
# If the letter is uppercase, replace it with lowercase
 if "A" <= letter <= "Z":
  letter(chr(ord(letter) +32)

# Add it to the result 
  result += letter

# Step 6: Print the final result