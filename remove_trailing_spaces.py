# Program: Remove Trailing Spaces  

text = input("Enter a string: ")  

while text and text[-1] == ' ':
    text = text[:-1]  

print("String without trailing spaces: '" + text + "'")