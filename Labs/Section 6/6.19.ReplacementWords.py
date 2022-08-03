# Get user's inputs.
user_replacement_pairs = input()
user_phrase = input()

# Convert user input to list from split.
user_replacement_pairs = user_replacement_pairs.split()

# Create new dictionary.
dict_replace = {}

# Cycle thru replacement pairs.
for idx, string in enumerate(user_replacement_pairs):
    # If index is the 1st in the pair, add it to the dictionary as a key.
    if idx % 2 == 0:
        dict_replace[string] = {}

    # Otherwise, set the value of the 1st element in the pair to the current string.
    else:
        dict_replace[user_replacement_pairs[idx - 1]] = string

# For each pair in the dictionary, update the user_phrase by making the replacements.
for word, replacement_word in dict_replace.items():
    user_phrase = user_phrase.replace(str(word), str(replacement_word))

# Output the updated phrase.
print(user_phrase)