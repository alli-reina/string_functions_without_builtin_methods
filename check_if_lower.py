# Program: Check if String is Lowercase  

text = input("Enter a string: ")  
is_lower = True  

for char in text:  
    if 'A' <= char <= 'Z':
        is_lower = False  

print(is_lower)
