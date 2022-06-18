import datetime

# Acts as a way to loop the questions if a valid response isn't given.
valid_response = False

def start():
    global valid_response

    print("What's your name?")
    name = input()

    # Repeat the question until there's a valid response.
    while not valid_response:
        print("How old are you?")

        try:
            age = int(input())
            valid_response = True
        except:
            print("Please enter an integer.")

    # Reset the variable for the next question.
    valid_response = False
    print("Have you had your birthday yet this year? (Y/N)")

    # Repeat the question until there's a valid response.
    while not valid_response:
        response = input().lower()

        if response == "y":
            # Already had birthday is 2022 - age.
            birth_year = datetime.datetime.now().year - age
            valid_response = True
        elif response == "n":
            # Not had birthday is 2021 - age.
            birth_year = datetime.datetime.now().year - 1 - age
            valid_response = True
        else:
            print("Invalid input. Have you had your birthday yet this year? (Y/N)")

    valid_response = False
    print(f"Hello {name}. You were born in {str(birth_year)}")