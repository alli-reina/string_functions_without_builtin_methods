# Program: Removing the string suffix  

# Ask the user to enter a string
text = input("Enter a string: ")

# Ask the user to enter a suffix to remove
suffix = input("Enter suffix to remove: ")

# Check if 'text' ends with 'suffix' if true remove
if text.endswith(suffix):
    text = text[:len(text) - len(suffix)]

# Print the modified string with single quotes
print("String without suffix: '" + text + "'")