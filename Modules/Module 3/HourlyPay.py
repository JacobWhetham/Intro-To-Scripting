# Define a start function for cleanliness and restarting.
def start():

    # Try/except for a ValueError to validate user input as a float. Output error and restart if invalid.
    try:
        user_hours = float(input("Enter hours worked: "))
    except ValueError:
        print("Please input a valid number.")
        start()
        return

    # Ensure the user's input is not negative.
    if user_hours < 0:
        print("You can't work negative hours!")
        start()
        return

    # Assign the overtime and regular hours based on the user's input.
    overtime = user_hours - 40 if user_hours > 40 else 0
    hours = 40 if user_hours > 40 else user_hours

    # Perform calculations.
    pay = hours * 20
    overtime_pay = overtime * 30
    total_pay = pay + overtime_pay

    # Output the user's pay, with a breakdown of each.
    print(f"Standard pay: ${pay:.2f}. Overtime pay: ${overtime_pay:.2f}. Total pay: ${total_pay:.2f}.")

# Start the program.
start()
