# Store the user's input to a string-type variable.
user_input = input()

# Split the user's input to determine the search term and the phrase to search.
input_values = user_input.split()

# Define the search term and phrase to search based on position:
# Search term is the first element, the rest is the phrase.
# Convert the list of input values to a string-type to use for counting.
search_term = input_values[0]
phrase_to_search = str(input_values[1:])

# Output the number of occurrences.
print(phrase_to_search.count(search_term))