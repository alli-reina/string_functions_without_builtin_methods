# Program: Center a string manually without using center()

# Get input from the user (string and total width)
input_string = input("Enter a string: ")
total_width = int(input("Enter the total width: "))

# Check if total width is too small
if total_width <= len(input_string):
    print("'" + input_string + "'")

else:
    # Compute the number of spaces needed
    spaces = (total_width - len(input_string)) // 2  

    # Add spaces before and after
    centered_string = " " * spaces + input_string + " " * spaces  