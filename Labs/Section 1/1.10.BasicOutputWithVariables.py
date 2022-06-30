# Establish a variable and assign it to the int-converted string from the user's input.
user_num = int(input('Enter integer:\n'))

# Remind the user what they typed in.
print(f'You entered: {user_num}')

# Perform basic math operations with exponents and output the result.
print(f'{user_num} squared is {user_num ** 2}')
print(f'And {user_num} cubed is {user_num ** 3} !!')

# Overwrite the @user_num variable. There's no need to declare a second variable.
user_num = int(input('Enter another integer:\n'))

# Perform basic math operations and output the result.
print(f'4 + {user_num} is {user_num + 4}')
print(f'4 * {user_num} is {user_num * 4}')