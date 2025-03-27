# Program: Manually Convert a String to Title Case

input_string = input("Enter a string: ")

if not input_string:
    print("Empty string.")
else:
    words = input_string.split()
    title_case_words = []

    for word in words:
        title_case_words.append(word[0].upper() + word[1:].lower())

    print(" ".join(title_case_words))