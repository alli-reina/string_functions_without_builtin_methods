# Program: Convert all uppercase letters to lowercase without using lower()

input_string = input("Enter a string: ")
result = ""

for letter in input_string:
    if "A" <= letter <= "Z":
        letter = chr(ord(letter) + 32)
    result += letter

print("Final string:", result)