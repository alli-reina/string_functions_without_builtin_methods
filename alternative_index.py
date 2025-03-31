# # Program: Get First Index of Character  

# Get user input as 'text'  
text = input("Enter a string: ")  

# Get user input as 'char' (character to find)  
char = input("Enter character to get index: ")  

# Set 'position' to -1
position = -1  

# Set 'start' to 0 (starting index)  
start = 0  

# Loop while 'start' is less than the length of 'text' and 'position' is -1  
while start < len(text) and position == -1:
    if text[i] == char:  
        position = i  
    start += 1
 
# If 'position' is -1, print "No letter found"  
if position == -1:  
    print("No letter found")  
# Else, print 'position'  
else:  
    print(position)