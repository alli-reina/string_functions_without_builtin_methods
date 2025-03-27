# Program: Remove leading spaces without using lstrip()

user_input = input("Enter a string: ")

index = 0
while index < len(user_input) and user_input[index] == " ":
    index += 1

result = user_input[index:]

print(result)