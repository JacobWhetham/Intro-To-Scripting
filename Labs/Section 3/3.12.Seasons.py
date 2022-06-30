# Define a function to start the program for cleanliness.
def start():
    # Create a dictionary to assign each season with its months.
    seasons = {
        "Spring": {"Months": ("March", "April", "May", "June"), "Marking_Dates": (20, 20)},
        "Summer": {"Months": ("June", "July", "August", "September"), "Marking_Dates": (21, 21)},
        "Autumn": {"Months": ("September", "October", "November", "December"), "Marking_Dates": (22, 20)},
        "Winter": {"Months": ("December", "January", "February", "March"), "Marking_Dates": (21, 19)}
    }

    # Create a dictionary to log the number of days in each month.
    max_days = {"January": 31, "February": 29, "March": 31, "April": 30,
                "May": 31, "June": 30, "July": 31, "August": 31,
                "September": 30, "October": 31, "November": 30, "December": 31}

    # Get the user's input for the month.
    user_month = input()

    # Prevent the user from inputting a non-integer for the day. Restart the program if invalid input.
    try:
        user_day = int(input())
    except ValueError:
        print("You need to input an integer!")
        start()
        return

    # Test if the user's input is not a valid month, or if the user's input is more than the max days
    # in the specified month, or if the integer is less than 1.
    # Notify user and restart if something is invalid.
    if (user_month not in max_days) or (user_day > max_days[user_month] or user_day < 1):
        print("Invalid")
        start()
        return

    # Cycle through each key(a season) in the seasons dictionary.
    for season in seasons:

        # If the user's month is not found in the Months key of the seasons dictionary.
        # Meaning, the user's month is not in that season, continue (test the loop again for the next season).
        if user_month not in seasons[season]["Months"]:
            continue

        # If the user's month is equivalent to the first element in the Months key.
        # Meaning, the start month of the season.
        if user_month == seasons[season]["Months"][0]:

            # If the user's day is less than the 1st element of the Marking_Dates key.
            # Meaning, the user's day is before the start of the season.
            if user_day < seasons[season]["Marking_Dates"][0]:
                # Go to next cycle since the month and day are before the season's start - the date is
                # in another season.
                continue

        # Otherwise, if the user's month is the last element in the season Months key.
        # Meaning, the end month of the season.
        elif user_month == seasons[season]["Months"][3]:
            # If the user's day is greater than the 2nd element of the Marking_Dates key.
            # Meaning, the user's day is after the end of the season.
            if user_day > seasons[season]["Marking_Dates"][1]:
                # Go to next cycle since the month and day are after the season's end - the date is
                # in another season.
                continue

        # Everything else makes the function restart, so anything below here is executed only
        # if the user's input matches a season.

        # Let the user know which season the date is in.
        print(f"{season}")

        # Leave the cycle, preventing further executions if the season was found.
        break


# Start the program.
start()
