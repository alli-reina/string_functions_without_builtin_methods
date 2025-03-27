# Program: Check if String Ends with Given Suffix

# Get input from the user for the main string
input_string = input("Enter the main string: ")

# Get input from the user for the suffix to check
suffix = input("Enter the suffix: ")

# Compare the last characters of the main string with the suffix
if input_string[-len(suffix):] == suffix:
    # If they match, print "Ends with given suffix"
    print("Ends with given suffix")
else:
    # Otherwise, print "Does not end with given suffix"
    print("Does not end with given suffix")