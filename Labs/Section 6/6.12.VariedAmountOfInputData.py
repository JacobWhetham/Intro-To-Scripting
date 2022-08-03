# Get user's input (can be multiple ints separated by spaces).
user_input = input()

# Get the max in the input thru splitting and converting each element to an int.
max_num = max([int(i) for i in user_input.split()])

# Get the average in the input thru splitting and converting each element to an int, then dividing by the length of the split.
avg_num = int(sum([int(i) for i in user_input.split()]) / len(user_input.split()))

# Output the average and max values.
print(avg_num, max_num)