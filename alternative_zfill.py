# Program: Zero Fill String  

text = input("Enter a string: ")  
width = int(input("Enter total width: "))  

if len(text) < width:  
    text = '0' * (width - len(text)) + text  

print("'" + text + "'")