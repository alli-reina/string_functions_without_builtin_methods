# Program: Get First Index of Character  

# Get user input as 'text'  
text = input("Enter a string: ")  

# Get user input as 'char' (character to find)  
char = input("Enter character to get index: ")  

# Set 'position' to -1
position = -1  

# Set 'i' to 0 (starting index)  
i = 0
  
# Step 5: Loop while 'i' is less than the length of 'text' and 'position' is -1  
#         If 'text[i]' is equal to 'char', set 'position' to 'i'  
#         Increase 'i' by 1  
# Step 6: If 'position' is -1, print "No letter found"  
#         Else, print 'position'