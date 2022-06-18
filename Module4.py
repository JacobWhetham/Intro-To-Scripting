import random

rand = 0;
won_game = False

def start():
    create_game()

def create_game():
    global rand, won_game;
    won_game = False

    # Repeat if invalid input.
    try:
        print("What's the minimum number?")
        low = int(input())
        print("And the maximum?")
        high = int(input())
    except:
        print("Please enter integers only.")
        create_game()

    # Repeat if numbers are not within valid range.
    if high < low:
        print(f"The high ({high}) must be larger than the low ({low}).")
        create_game()
    elif high == low:
        print(f"The high ({high}) cannot be the same as the low ({low}).")
        create_game()

    rand = random.randint(low, high)
    play_game()

def play_game():
    global rand, won_game

    # While the game is still being played.
    while not won_game:
        print("What's your guess?")

        # Repeat if guess is not an integer.
        try:
            guess = int(input())
        except:
            print("Please enter an integer only.")
            play_game()

        # End the game if the player wins, otherwise continue.
        if (guess == rand):
            won_game = True
            end_game();
        elif(guess > rand):
            print("Too high. Try again.")
            play_game()
        elif(guess < rand):
            print("Too low. Try again.")
            play_game()

def end_game():
    global won_game

    if won_game == True:
        print("Congrats, you won! Want to play again? (Y/N)")

    replay = input().lower()

    # Repeat if invalid input, replay or quit.
    if replay == "y":
        print("Good luck!")
        create_game()
    elif replay == "n":
        print("Thanks for playing. Bye!")
    else:
        print("Input invalid. Would you like to play again? (Y/N)")
        end_game()