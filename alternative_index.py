# Program: Get index of Character on a string

text = input("Enter a string: ")  
char = input("Enter character to get index: ")  

position = -1  
start = 0  

while start < len(text) and position == -1:  
    if text[start] == char:  
        position = start  
    start += 1  

if position == -1:  
    print("No letter found")  
else:  
    print(position)