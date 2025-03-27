# Program: Manual Implementation of ljust()

input_string = input("Enter a string: ")
width = int(input("Enter the desired width: "))

if len(input_string) < width:
    input_string += " " * (width - len(input_string))

print(f"'{input_string}'")