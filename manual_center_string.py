# Program: Center a string manually without using center()

input_string = input("Enter a string: ")
total_width = int(input("Enter the total width: "))

if total_width <= len(input_string):
    print("'" + input_string + "'")
else:
    spaces = (total_width - len(input_string)) // 2
    print("'" + " " * spaces + input_string + " " * spaces + "'")