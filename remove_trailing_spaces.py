BEGIN  
    # Ask the user to enter a string  
    PRINT "Enter a string: "  
    INPUT text  

    # Keep checking if the last character is a space  
    WHILE text is not empty AND last character is a space  
        # Remove the last space  
        REMOVE last character from text  

    # Display the final string with single quotes around it  
    PRINT "String without trailing spaces: '" + text + "'"  
END