# Program: Check if String Starts with Given Text  

text = input("Enter a string: ")  
start = input("Enter the starting text to check: ")  

is_start = True  

for i in range(len(start)):  
    if i >= len(text) or text[i] != start[i]:  
        is_start = False  
        break  

print(is_start)
