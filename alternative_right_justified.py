# Program: Right Justify String  

text = input("Enter a string: ")  
width = int(input("Enter total width: "))  

if len(text) < width:  
    text = ' ' * (width - len(text)) + text  

print("'" + text + "'")