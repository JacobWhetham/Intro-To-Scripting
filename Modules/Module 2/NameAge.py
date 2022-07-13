# Importing datetime for the .now() method to get the current year.
import datetime


# Define a method named start to run on program start.
def start():
    # Assign the user's input to a string-type variable for their name.
    name = input("What is your name? ")

    # Attempt to set an integer-type variable for the user's input. Except a ValueError in case the user types in a non-integer.
    try:
        age = int(input("How old are you? "))
    except ValueError:
        # Inform the user of their error and restart the method. Return to prevent looping error.
        print("You need to input an integer! Please try again.")
        start()
        return

    # Confirm whether the user's birthday has passed and save the input to a string-type variable.
    # Make the stored value lowercase for easy comparison.
    birthday_passed = input("Has your birthday passed yet this year? (Y/N): ").lower()

    # Assign an integer-type variable as a placeholder for the user's birth year.
    birth_year = 0

    # Assign a variable to the current year to make calculation look cleaner.
    current_year = datetime.datetime.now().year

    # Check for invalid input, i.e. anything other than "y" (yes) or "n" (no). Return to prevent looping error.
    if birthday_passed != "y" and birthday_passed != "n":
        # Inform the user of error and restart the method.
        print("Invalid input. Please try again.")
        start()
        return

    # If the user's birthday has already passed, their birth year is just the current year minus their age.
    elif birthday_passed == "y":
        birth_year = current_year - age

    # Otherwise (their birthday has not passed), their birth year is the last year (current year - 1) minus their age.
    else:
        birth_year = (current_year - 1) - age

    # Output the result.
    print(f"Hello {name}! You were born in {birth_year}.")


# Call the start method upon program running.
if __name__ == "__main__":
    start()
