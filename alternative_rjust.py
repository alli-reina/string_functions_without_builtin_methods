# Program: Get Last Index of Character

# Get user input as 'text' and 'char'
text = input("Enter a string: ")
char = input("Enter character to get last index: ")

# Set 'position' to -1
position = -1

# Loop backwards from the last index of 'text'
start = len(text) - 1
while start >= 0:
    # If 'text[start]' equals 'char', set 'position' to 'start' and exit loop
    if text[start] == char:
        position = start
        break
    start -= 1