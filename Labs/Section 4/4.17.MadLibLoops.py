# Define function to call from while loop.
def getInput():
    # Split the user's input.
    split_string = input().split()
    # Return @split_string as a callback.
    return split_string


# Create infinite loop.
while True:
    # Call function to get user's input as a list.
    split_string = getInput()

    # Split the list to get individual variables.
    noun = split_string[0]
    number = int(split_string[1])

    # If the user input 'quit'.
    if noun == "quit":
        # Exit the infinite loop.
        break

    # Output the mad lib. Only gets called if the loop was not exited.
    print(f"Eating {str(number)} {noun} a day keeps the doctor away.")