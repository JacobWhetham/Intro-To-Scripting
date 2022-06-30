# FIXME (1): Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
favorite_flower = input('Enter favorite flower:\n')
favorite_number = input('Enter favorite number:\n')

print("You entered: {} {} {}".format(favorite_color, favorite_flower, favorite_number))

# FIXME (2): Output two password options
password1 = "_".join([favorite_color, favorite_flower])
password2 = f"{favorite_color}".join([favorite_number, favorite_number])
print('\nFirst password: {}'.format(password1))
print('Second password: {}\n'.format(password2))


# FIXME (3): Output the length of the two password options
print("Number of characters in {}: {}".format(password1, len(password1)))
print("Number of characters in {}: {}".format(password2, len(password2)))