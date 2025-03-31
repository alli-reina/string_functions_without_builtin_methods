# Program: Zero Fill String  

# Get user input as 'text' 
text = input("Enter a string: ")  
# Get user input as 'width' (total desired width)
width = int(input("Enter total width: "))

# Check if the length of 'text' is less than 'width'  
if len(text) < width:  
    text = '0' * (width - len(text)) + text

# Step 4: Print the zero-filled 'text' with single quotes