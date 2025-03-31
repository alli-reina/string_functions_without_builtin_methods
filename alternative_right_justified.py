# Program: Right Justify String  

# Get user input as 'text'
text = input("Enter a string: ")
# Get user input as 'width' (total desired width)
width = int(input("Enter total width: "))

# Check if the length of 'text' is less than 'width'
if len(text) < width:  
    text = ' ' * (width - len(text)) + text
    
# Print the right-justified 'text'
print("'" + text + "'")