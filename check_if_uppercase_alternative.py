# Program: Check if all characters are uppercase without using isupper()

# Get input from the user
input_string = input("Enter a string: ")

# Check if all characters are uppercase
all_upper = True  

for letter in input_string:
    # If a lowercase letter is found, set all_upper to False
    if "a" <= letter <= "z":
        all_upper = False
        break  

# Print the result
if all_upper:
    print("All uppercase")
else:
    print("Not all uppercase")