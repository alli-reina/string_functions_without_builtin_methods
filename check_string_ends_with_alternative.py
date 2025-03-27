# Program: Check if String Ends with Given Suffix

input_string = input("Enter the main string: ")
suffix = input("Enter the suffix: ")

if input_string[-len(suffix):] == suffix:
    print("Ends with given suffix")
else:
    print("Does not end with given suffix")