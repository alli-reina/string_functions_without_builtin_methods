# Program: Removing the string suffix  

text = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")

if text.endswith(suffix):
    text = text[:len(text) - len(suffix)]

print("String without suffix: '" + text + "'")