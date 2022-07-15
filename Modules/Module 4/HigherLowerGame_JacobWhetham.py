# Import random to create a random int.
import random

# Create function for recalling game on replay request.
def play_game():
    # Create an infinite loop to run the game until stopped.
    while True:
        # Try/Except in case of invalid input.
        try:
            # Get and assign the user's inputs for the game's parameters.
            lower_bound = int(input("What's the minimum value?"))
            higher_bound = int(input("What's the maximum value?"))
        except ValueError:
            # Output an error and restart the loop if invalid inputs were given.
            print("Integers only please.")
            continue

        # If the maximum value is higher or equal to the minimum value, output an error and restart.
        if higher_bound <= lower_bound:
            print("The maximum value has to be higher than the minimum.")
            continue

        # Create and assign a random int using the user's input.
        rand_num = random.randrange(lower_bound, higher_bound)

        # Create another infinite loop to handle the player's guessing.
        while True:
            # Try/Except to test for valid input.
            try:
                # Assign the player's input as a guess.
                guess = int(input("What's your guess?"))
            except ValueError:
                # Output an error and restart this infinite loop if input was invalid.
                print("Integers only please.")
                continue

            # If the user's guess matches the random int, inform the user they won and see if they want to replay.
            if guess == rand_num:
                print("You win!")
                replay = input("Play again? (Y/N)")

                # If the user did not answer properly, give them an error and retry.
                while replay.capitalize() != "N" and replay.capitalize() != "Y":
                    print("Please enter 'y' or 'n'!")
                    replay = input("Play again? (Y/N)")

                # If the user answered no, quit the program.
                if replay.capitalize() == "N":
                    quit()

                # If the user answered yes, restart the game by breaking out of this infinite loop (returning to main loop.)
                elif replay.capitalize() == "Y":
                    break

            # If the user's guess is less than the random int, tell them to guess higher and restart the loop.
            if guess < rand_num:
                print("Higher")
                continue

            # Otherwise, the user's guess is lower than the random int. Tell them to guess lower. The while loop
            # will automatically restart at this point because it's an infinite loop.
            else:
                print("Lower")

# Start the game by calling the containing function.
play_game()