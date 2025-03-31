# Program: Count Occurrences in String  

text = input("Enter a string: ")  
char = input("Enter character to count: ")  

count = 0  

for c in text:  
    if c == char:  
        count += 1  

print(count)