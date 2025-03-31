# Start the program
BEGIN  

    # Ask the user to enter a string
    PRINT "Enter a string: "  
    INPUT text  

    # Loop while text is not empty and the last character is a space
    WHILE text is not empty AND last character of text is a space  
        # Remove the last character from text
        REMOVE the last character from text  

    # Print the result with single quotes around the text
    PRINT "String without trailing spaces: '" + text + "'"  

# End the program