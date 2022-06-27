import main

# NOTE: This "game" is incomplete. It is for educational purposes and will probably remain incomplete as it shows the
# necessary skillsets to accurately recreate and learn from this project.

# World Map:
"""
[0,4][ x ][ x ][ x ][ x ]
[0,3][ x ][ x ][ x ][ x ]
[0,2][1,2][ x ][ x ][ x ]
[0,1][ x ][ x ][ x ][ x ]
[0,0][ x ][ x ][ x ][ x ]
"""


# Dictionaries to test for checkpoints.
player_inventory = {"sword": False, "shield": False, "amulet": False, "armor": False, "scroll": False, "potion": False}
able_directions = {"north": True, "east": True, "south": True, "West": True}
player_dialogue_checklist = {"Start":False, "Meadow": False,"Chapel":False, "Lake":False}

# List to keep track of the room the player is in. Coordinate system.
player_position = [0, 0]

# Acts as a flag if there is an item in the room, and can be tested against with player commands.
item_in_area = ""


def start():
    load_level(player_position)


def load_level(player_pos):
    global player_dialogue_checklist, item_in_area, player_position

    print("-------------------------------------------------------------------------------------")

    # Perform different actions depending on which room is entered based on the coordinates received.
    match player_pos:
        case (0, 0):
            # Set which directions the player can move from here.
            change_walkable(True, False, False, False)

            if not player_dialogue_checklist["Start"]:
                print("You awaken on the floor of a lightly furnished stone chamber.")
                print("'So you're awake.'")
                print("You look to see a withered old man sitting on the floor in front of you.")
                print("'I thought you would die when I saw you.'")
                print("You try to sit up. Your body is stiff and aching. You notice bloodsoaked bandages wrapped tightly around you.")
                print("'Here. Take this.'")
                print("The man places a mysterious glowing potion before you.")
                print("'Gather yourself and grow stronger before you tackle him again.'")
                print("The man begins to crumble into a fine ash.")
                print("You see a wooden door to your north.")

                # Update dialogue checkpoint to prevent replaying the same dialogue on reentry.
                player_dialogue_checklist["Start"] = True

            else:
                print("This place seems oddly familiar.")
                print("You recall this is where you awoke to see the old man.")
                print("The door outside lies to the north.")

                if not player_inventory["potion"]:
                    print("The potion still lay on the floor where he left it.")

            if not player_inventory["potion"]:
                item_in_area = "potion"

        case (0, 1):
            change_walkable(True, False, True, False)

            if not player_dialogue_checklist["Meadow"]:
                print("The light outside blinds you temporarily.")
                print("As you stumble forth, you begin to see green fields with large groups of asters.")
                print("You take a look at the humble abode, it is a quaint cabin on the outskirts of a meadow.")
                player_dialogue_checklist["Meadow"] = True

            else:
                print("The meadow is just as you remember it.")

            print("A dirt path runs from the cabin to the north.")
            print("The cabin lies to your south.")

        case (0, 2):
            change_walkable(True, True, True, False)
            print("The path has come to a crossroads.")
            print("To the east you can see a lake sparkling in the distance.")
            print("To the north the dirt path extends further than your sight allows.")
            print("To your west lies a dense forest. Navigating through it all would be a waste of time.")
            print("The meadow is to your south.")

        case (0, 3):
            change_walkable(True, False, True, False)
            print("A dense fog beings to surround you as you continue marching north.")
            print("Though close, you can barely make out the faint shadows of a structure through the thick fog.")
            print("As you approach the large structure, your hair begins to stand on end.")
            print("You are close enough to make out the structure as a chapel.")
            print("You near the doubledoors of the chapel to the north.")
            print("To the south lie the crossroads.")
            print("You do not feel safe traveling off the path to the east or west.")

        case (0, 4):
            change_walkable(False, False, True, False)

            if not player_dialogue_checklist["Chapel"]:
                print("You knock loudly on the chapel's doors and wait a moment before knocking again.")
                print("There is no answer.")
                print("You push the heavy oak doors open, allowing you to pass through.")
                print("The doors slam shut behind you with a mighty crash.")
                print("You look around the room and see the chaos that has befallen this place.")
                print("The pews are thrown about, many of them completely overturned. Scraps of paper litter the floor.")
                print("You see a robed man laying at the pulpit facing away from you.")
                print("As you approach the man, you hear his raspy breathing - a death rattle.")
                print("You place your arm on the man's shoulder and he turns his head to you.")
                print("'He must not get it. Do not let him have it.'")
                print("The man gestures to an empty bookshelf surrounded by books that looked as if tossed to the ground.")
                print("You look back to the man but see he has already passed.")
                print("You approach the bookshelf and examine it.")
                print("As you run your hand along one of the shelves, you feel it shift.")
                print("You remove the shelf to find a hidden compartment bored into the shelf's spine.")
                print("Inside the spine is a scroll.")
                print("The doors of the chapel lie to the south.")
                player_dialogue_checklist["Chapel"] = True

            else:
                print("This place is still just as messy.")

                if not player_inventory["scroll"]:
                    print("You recall the scroll hiding in the bookshelf.")

            if not player_inventory["scroll"]:
                item_in_area = "scroll"

        case (1, 2):
            change_walkable(False, False, False,True)
            print("You can only go West.")

        # If nothing matches, send player to a void where they are sent back to the starting room.
        # This also can be used if the player was killed. Load a non-level after death, e.g. load_level(999,999)
        case _:
            change_walkable(False, False, False, False)
            print("You cannot see into the dark void before you.")
            print("You hear the stamping of footsteps in front of you.")
            print("A ghastly whisper speaks to you.")
            print("'You should not be here. Go now.'")
            print("The air around you thrashes violently as you begin to feel faint.")
            print("You open your eyes to see you are now elsewhere.")

            # Send player back to the starting room.
            player_position = (0,0)
            load_level(player_position)

    await_input()


def move_player(direction):
    global player_position

    # Modify the cooresponding coordinate based on direction input. Test if valid direction.
        # North = +y, South = -y, East = +x, West = -x
    try:
        if able_directions[direction]:
            match direction:
                case "north":
                    player_position[1] += 1
                case "east":
                    player_position[0] += 1
                case "south":
                    player_position[1] -= 1
                case "west":
                    player_position[0] -= 1

            load_level(player_position)
        else:
            print("You cannot go that direction.")

    except:
        print("Confused, you find yourself entering the area again.")

    await_input()


def change_walkable(north_able, east_able, south_able, west_able):
    global able_directions

    # Update list to match input, setting the valid directions the player can move.
    able_directions["north"] = north_able
    able_directions["east"] = east_able
    able_directions["south"] = south_able
    able_directions["west"] = west_able


def player_commands(command):
    global able_directions, item_in_area

    # Remove case-sensitivity by turning the input into a lower-case form.
    command = command.lower()

    # If the command starts with a character or string of characters:
    if command.startswith("go"):
        # Split the command (the default separator is white space), take the second group of separated word (the
        # direction) and set it to a string variable for future use.
        direction = command.split()[1]

        # Send the direction to the move_player() method for further processing.
        move_player(direction)
    elif command.startswith("take"):
        item = command.split()[1]

        # If the item the player typed matches the name of the item in the area, they can take it.
        if item == item_in_area:
            take_item(item)
        else:
            print(f"There is no {item} here to take.")
            await_input()

    elif command == "check inventory":
        check_inventory()
    elif command == "quit":
        main.start()
    else:
        print("That command isn't valid. Try 'take <item>', 'go <direction>' or 'quit'.")
        await_input()


def take_item(item):
    global player_inventory, item_in_area

    # Add the item to the inventory by triggering a flag. A list may be better, but our dictionary is set to use a
    # dictionary because we are using a small amount of items and a simple system to access them with little coding.
    player_inventory[item] = True
    item_in_area = ""
    print(f"You've picked up the {item}.")
    await_input()


def check_inventory():
    global player_inventory

    items_for_dialogue = []

    # Add each item that is set to True (player has it) to the list.
    for item in player_inventory:
        if item:
            items_for_dialogue.append(item)

    await_input()

    # Output the list.
    print(f"You are carrying the following items: {items_for_dialogue}")


def await_input():
    # Get players input and test it.
    print("What do you do?")
    command = input()
    player_commands(command)
