# Program: Remove a prefix manually without using removeprefix()

input_string = input("Enter a string: ")
prefix = input("Enter a prefix to remove: ")

if input_string.startswith(prefix):
    result_string = input_string[len(prefix):]
else:
    result_string = input_string

print("Final string:", result_string)