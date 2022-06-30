# Define the start function for cleanliness.
def start():
    # Try/catch a ValueError to prevent the user from breaking the code by using anything other than an int.
    try:
        # Initialize variables to store user input.
        int_1 = int(input())
        int_2 = int(input())
        int_3 = int(input())

    except ValueError:
        # Let the user know they messed up, restart the program.
        print("You need to enter integers only!")
        start()
        return

    # Establish a list using all the variables.
    temp_list = [int_1, int_2, int_3]

    # Output the minimum value of the list.
    print(min(temp_list))


start()

"""
Alternate code to show knowledge of the relation operators... just in case:

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
min = 0

if (num_1 >= num_2):
    min = num_2
elif (num_2 > num_1):
    min = num_1

if (min > num_3):
    min = num_3

print(min)
"""