# Program: Convert to Uppercase  

text = input("Enter a string: ")  
uppercase_text = ""  

for char in text:  
    if 'a' <= char <= 'z':  
        uppercase_text += chr(ord(char) - 32)  
    else:  
        uppercase_text += char  

print("Uppercase string: '" + uppercase_text + "'")