from enum import Enum

# Enum of directions to prevent typos when accessing directions.
class Directions(Enum):
    North = "north"
    South = "south"
    West = "west"
    East = "east"

# Enum of rooms using coordinate layout for easy reference, e.g. not memorizing or referencing coordinates.
class Rooms(Enum):
    Dungeon = (0, 0)
    Dining_Room = (0, 1)
    Wine_Cellar = (0, 2)
    Foyer = (-1, 0)
    Kitchen = (-1, 1)
    Pantry = (-1, 2)
    Closet = (-2, 0)
    Elevator = (-2, 1)
    Villain_Chamber = (999, 999)

# Enum of items to maximize accuracy when working with items, e.g. adding an item to the player's inventory.
class Items(Enum):
    Feather = "feather"
    Vial_of_Water = "vial of water"
    Pantry_Key = "pantry key"
    Elevator_Key = "elevator key"
    Shoelace = "shoelace"
    Potatoes = "sack of potatoes"

# Flavor variables, fun tid-bits to keep track of and potentially use.
player_incorrect_direction_count = 0
player_cheat_attempts = 0

# Intialize variables.
player_position = Rooms.Dungeon
player_inventory = []
dialogue_checkpoints = {}

# Keep track of the state of dialogue - no repeating conversations.
room_dialogue_state = {Rooms.Dungeon: 0,
                       Rooms.Dining_Room: 0,
                       Rooms.Wine_Cellar: 0,
                       Rooms.Foyer: 0,
                       Rooms.Kitchen: 0,
                       Rooms.Pantry: 0,
                       Rooms.Closet: 0,
                       Rooms.Elevator: 0,
                       Rooms.Villain_Chamber: 0}

# Define the directions the player can move from in each room.
room_directions = {Rooms.Dungeon: [Directions.North.value],
                   Rooms.Dining_Room: [Directions.South.value, Directions.West.value],
                   Rooms.Wine_Cellar: [Directions.West.value],
                   Rooms.Foyer: [Directions.North.value, Directions.West.value],
                   Rooms.Kitchen: [Directions.North.value, Directions.South.value, Directions.West.value, Directions.East.value],
                   Rooms.Pantry: [Directions.South.value, Directions.East.value],
                   Rooms.Closet: [Directions.East.value],
                   Rooms.Elevator: [Directions.East.value],
                   Rooms.Villain_Chamber: []}

# Define where the items are throughout the map.
item_locations = {Items.Vial_of_Water: Rooms.Kitchen,
                  Items.Feather: Rooms.Dining_Room,
                  Items.Shoelace: Rooms.Closet,
                  Items.Potatoes: Rooms.Pantry,
                  Items.Pantry_Key: Rooms.Foyer,
                  Items.Elevator_Key: Rooms.Wine_Cellar}

# Define what items are needed to enter certain rooms.
room_items_needed = {Rooms.Pantry: Items.Pantry_Key,
                     Rooms.Wine_Cellar: Items.Pantry_Key,
                    Rooms.Elevator: [Items.Vial_of_Water, Items.Shoelace, Items.Elevator_Key, Items.Feather, Items.Potatoes, Items.Pantry_Key]}

def load_room(room):
    """
        Loads the specified room. Argument is a (x, y) tuple.

        Does different things depending on the room that was loaded.
        Displays dialogue based on the state of the dialogue for that room, which is then itself updated.
    """

    print(f"You've entered the {room.name.lower()}.")

    match room:
        case Rooms.Dungeon:
            if room_dialogue_state[room] == 0:
                pass
        case Rooms.Dining_Room:
            pass
        case _:
            pass

def update_player_position(direction):
    """
        Updates the player position and calls to load the next room.

        Note: @player_position is the room (Enum) the player is in, not an (x, y) coordinate.

        Modifies the player's coordinates based on the direction argument. Then, looks for the room associated with the
        player's coordinates.

        Cancels loading the room if the player does not have the required items.
    """

    global player_position
    player_coordinates = [player_position.value[0], player_position.value[1]]

    match direction:
        case Directions.North:
            player_coordinates[1] += 1
        case Directions.South:
            player_coordinates[1] += -1
        case Directions.West:
            player_coordinates[0] += -1
        case Directions.East:
            player_coordinates[0] += 1

    player_coordinates = (player_coordinates[0], player_coordinates[1])

    if Rooms(player_coordinates) in room_items_needed:
        if room_items_needed[Rooms(player_coordinates)] not in player_inventory:
            print(f"You don't have all the materials needed to proceed.")
            print(f"You're still in the {player_position.name.lower()}.")
            return

    player_position = Rooms(player_coordinates)
    load_room(player_position)


def start_game():
    """Starts the game by loading the first level and placing the player in an infinite loop."""
    load_room(Rooms.Dungeon)

    while True:
        response = input("What do you do?")
        test_response(response)

def test_response(response):
    """
        Tests the player's response for validity and calls the corresponding function.

        Makes user input case-insensitive by lowering it. Turns user input into a list of words and tests the first word
        against several keywords. Performs different functions based on the keyword.

        Checks for errors, i.e. trying to take an item that doesn't exist or that is in a different room.

        Keywords:

        quit - Quits the game.
        go <direction> - Attempts to travel in the direction.
        take <item> - Attempts to take the item.
        inventory - Displays the player's inventory.
    """
    global player_incorrect_direction_count, player_cheat_attempts

    response = response.lower()
    response = response.split()

    match response[0]:
        case "quit":
            quit()

        case "go":
            if response[1] in room_directions[player_position]:
                update_player_position(Directions(response[1]))
            else:
                print("You can't go that way!")
                player_incorrect_direction_count += 1

        case "take":
            try:
                item = Items(' '.join(response[1:]))
            except:
                print("That item doesn't exist!")
                return

            if player_position == item_locations[item] and item not in player_inventory:
                player_inventory.append(item)
                print(f"You picked up the {item.value}.")

            elif item in player_inventory:
                print("You already picked that up, remember?")

            elif player_position != item_locations[item]:
                print("How do you plan to pick up something from another room?")
                player_cheat_attempts += 1

        case "inventory":
            items = []

            for item in player_inventory:
                items.append(item.value)

            print(f"You are currently carrying: {', '.join(items)}")

        case _:
            print("Unknown command. Please try 'go DIRECTION', 'take ITEM', 'quit', or 'inventory'.")

# Start the game at program run.
if __name__ == "__main__":
    start_game()