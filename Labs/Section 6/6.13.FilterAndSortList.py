# Get the user's input.
user_input = input()

# Create a new list from a conditional list comprehension thru splitting input and converting elements to int.
pos_nums = [int(i) for i in user_input.split() if int(i) >= 0]

# Sort the list.
pos_nums.sort()

# Print each element in pos_nums with a trailing space.
for num in pos_nums:
    print(num, end=' ')