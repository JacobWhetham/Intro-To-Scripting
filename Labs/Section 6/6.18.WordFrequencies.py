# Get user input.
user_input = input()

# Create a list based on splitting the user input.
user_phrase = user_input.split()

# Output each word in the list and its corresponding frequency.
for word in user_phrase:
    print(f"{word} {user_phrase.count(word)}")