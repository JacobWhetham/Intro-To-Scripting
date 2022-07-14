# Get the user's inputs for the character to use and the triangle's height.
triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

# Output an empty line for formatting purposes.
print()

# Loop through a range of the triangle's height (add + 1 since range excludes the maximum value).
for i in range(1, triangle_height + 1):
    # Output the characters with a trailing space @i times - for formatting.
    print(f"{triangle_char} " * (i))