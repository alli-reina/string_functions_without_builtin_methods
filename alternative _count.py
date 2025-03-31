# Program: Count Occurrences in String  

# Get user input as 'text'
text = input("Enter a string: ")    
# Get user input as 'char' (character to count)
char = input("Enter character to count: ")

# Set 'count' to 0
count = 0
  
# Loop through each character in 'text'
for letter in text:  
    if letter == char:  
        count += 1 

# Print 'count'
print(count)