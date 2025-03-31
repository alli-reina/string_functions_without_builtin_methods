# Program: Get Last Index of Character

text = input("Enter a string: ")
char = input("Enter character to get last index: ")

position = -1
start = len(text) - 1

while start >= 0:
    if text[start] == char:
        position = start
        break
    start -= 1

if position == -1:
    print("No letter found")
else:
    print(position)