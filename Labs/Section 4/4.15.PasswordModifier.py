# Get the user's input.
word = input()

# Establish a password variable for later storage.
password = ''

# Reassign input with all occurrences of certain characters.
word = word.replace('i', '!')
word = word.replace('a', '@')
word = word.replace('m', 'M')
word = word.replace('B', '8')
word = word.replace('o', '.')

# Reassign @password to the modified input + 'q*s'.
password = word + 'q*s'

# Output password.
print(password)