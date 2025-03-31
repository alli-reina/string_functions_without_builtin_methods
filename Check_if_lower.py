# Program: Check if String is Lowercase  

# Get user input as 'text'
text = input("Enter a string: ")
 
# Set 'is_lower' to True
is_lower = True

# If the character is between 'A' and 'Z', set 'is_lower' to False
for char in text:  
    if 'A' <= char <= 'Z':
        is_lower = False  

# Print 'is_lower'
print(is_lower)