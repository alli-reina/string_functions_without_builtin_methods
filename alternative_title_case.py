# Program: Manually Convert a String to Title Case

# Get input from the user
input_string = input("Enter a string: ")

# Check if the string is empty
if not input_string:
    print("Empty string.")
else:
    # Split the string into words
    words = input_string.split()

# Convert each word to title case manually
    title_case_words = []
    for word in words:
        title_case_word = word[0].upper() + word[1:].lower()
        title_case_words.append(title_case_word)

    # Join the words back into a single string
    result = " ".join(title_case_words)

    # Display the result
    print(result)