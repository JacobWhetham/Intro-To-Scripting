# Establish and assign variables based on user input. Convert types as needed for future use.
user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_char = input('Enter character:\n')
user_string = input('Enter string:\n')

# Establish list-type variable to store the user inputs for later iteration.
user_list = [user_int, user_float, user_char, user_string]


# Create function to handle list iteration and output, using a list-type as an argument.
def output_list(output):
    # Iterate through the list argument.
    for item in output:

        # Get the index of each item in the list.
        index = output.index(item)

        # If the index is the last item in the list (len() starts counting from 1 instead of 0, so len() - 1 = last index):
        if index == len(output) - 1:

            # Output the item at the index with a trailing newline.
            print(output[index])

        # Otherwise, output the item at the index with a trailing whitespace.
        else:
            print(output[index], end=' ')


# Call the function and submit @user_list as an argument.
output_list(user_list)

# Update @user_list to itself with a negative slice (reversing the list).
user_list = user_list[::-1]

# Call the function and submit the reversed list as an argument.
output_list(user_list)

# Output the character associated with the value of @user_int.
print(f"{user_int} converted to a character is {chr(user_int)}")