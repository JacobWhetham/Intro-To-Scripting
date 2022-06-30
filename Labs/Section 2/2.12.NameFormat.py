# Get the user's input as a string-type variable.
name = input()

# Split the user's input utilizing whitespace as a seperator.
split_name = name.split()

# Create a string-type variable for future printing using the last element of the split user's input.
# Concatenate string with a comma and space for formatting.
output = split_name[-1] + ", "

# Cycle through the split user's input, ignoring the last element.
for element in split_name[:-1]:
    # Get the index of the current element in the cycle.
    index = split_name.index(element)

    # Update the output variable by concatenating to it with the first character of the current element.
    # Add a trailing period for formatting.
    output = output + split_name[index][0] + "."

# After the cycle, print the output.
print(output)