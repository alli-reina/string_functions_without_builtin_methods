# Program: Get First Index of Character  

# Get user input as 'text'  
text = input("Enter a string: ")  

# Get user input as 'char' (character to find)  
char = input("Enter character to get index: ")

# Step 3: Set 'position' to -1 (default if character is not found)  
# Step 4: Set 'i' to 0 (starting index)  
# Step 5: Loop while 'i' is less than the length of 'text' and 'position' is -1  
#         If 'text[i]' is equal to 'char', set 'position' to 'i'  
#         Increase 'i' by 1  
# Step 6: If 'position' is -1, print "No letter found"  
#         Else, print 'position'