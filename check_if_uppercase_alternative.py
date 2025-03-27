# Program: Check if all characters are uppercase without using isupper()

# Get input from the user
input_string = input("Enter a string: ")

# Check if all characters are uppercase
all_upper = True

for letter in input_string:

# Step 3: If a letter is lowercase, print "Not all uppercase" and stop  
# Step 4: If no lowercase letters are found, print "All uppercase"