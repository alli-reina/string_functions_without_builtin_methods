# Program: Check if String Starts with Given Text  

# Get user input as 'text'
text = input("Enter a string: ")
  
# Get user input as 'start' (the text to check)
start = input("Enter the starting text to check: ")

# Set 'is_start' to True
is_start = True
 
# Loop through each character in 'start'
for i in range(len(start)):  
    if i >= len(text) or text[i] != start[i]:  
        is_start = False  
        break

# Step 5: Print 'is_start'