# Get the user's input and assign it to variables. Convert to integer-types for future use.
user_num = int(input())
x = int(input())

# Set an integer-type variable for use in a while loop.
i = 0

# While @i is less than 3:
while i < 3:
    # Update @user_num with itself divided by 3. Convert to integer type to remove decimals.
    user_num = int(user_num / x)

    # if @i is equivalent to 2 (the last iteration), output with no whitespace.
    if i == 2:
        print(user_num, end='')
    # Otherwise, output with whitespace for clarity.
    else:
        print(user_num, end=' ')

    # Increment @i before the next iteration, preventing an infinite loop.
    i += 1

# Print a newline after the rest of the program finishes.
print()