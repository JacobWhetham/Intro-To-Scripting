"""
    Programmer: Jacob Whetham
    Purpose: SNHU IT140 | Module Six Milestone (Movement Between Rooms)
"""

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# Initialize the player's starting position as the Great Hall.
player_pos = 'Great Hall'

# Define a function to run the game.
def play_game():
    # Prevent out-of-scope errors by marking the variable as global.
    global player_pos

    # Create an infinite loop for the game to run in.
    while True:
        # Output a prompt to the user and capture their input. Modify the input to prevent case-sensitivity.
        user_input = input(f"You are in the {player_pos}. What is your command?")
        user_input = user_input.capitalize()

        # Test if the user is quitting the game. If so, output prompt and quit game.
        if user_input == "Quit" or user_input == "Exit":
            print('Thanks for playing. Bye!')
            quit()

        # Test if the user's response (a cardinal direction) is in the available directions for the room based on the
        # dictionary. If so, update the player's position with the room associated with the direction. Output the
        # updated position to the player.
        if user_input in rooms[player_pos]:
            player_pos = rooms[player_pos][user_input]
            print(f'You have entered the {player_pos}.')

        # If the user input a valid cardinal direction, but it was not in the dictionary, inform the player they cannot
        # travel in that direction.
        elif (user_input == "North") or (user_input == "South") or (user_input == "East") or (user_input == "West"):
            print(f"You can't go that way!")

        # Otherwise, output an error to the user and prompt them about the valid commands.
        else:
            print('Invalid command. Please enter a cardinal direction or use "quit" or "exit" to end the game.')

# Start the game on running the python file.
if __name__ == "__main__":
    play_game()
