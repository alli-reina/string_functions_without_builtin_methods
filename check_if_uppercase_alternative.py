# Program: Check if all characters are uppercase without using isupper()

input_string = input("Enter a string: ")
all_upper = True  

for letter in input_string:
    if "a" <= letter <= "z":
        all_upper = False
        break  

if all_upper:
    print("All uppercase")
else:
    print("Not all uppercase")