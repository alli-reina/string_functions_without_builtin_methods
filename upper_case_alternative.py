# Program: Convert to Uppercase  

# Get user input as 'text'
text = input("Enter a string: ")
# Initialize an empty string 'uppercase_text' 
uppercase_text = ""  

# If it's a lowercase letter, convert to uppercase  
for char in text:  
    if 'a' <= char <= 'z':  
        uppercase_text += chr(ord(char) - 32)
    # Otherwise, keep it unchanged
    else:  
        uppercase_text += char
          
# Print the modified string
print("Uppercase string: '" + uppercase_text + "'")