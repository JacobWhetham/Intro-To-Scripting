# Create start function for cleanliness.
def start():
    # Get the user's input. Use try/except to catch error-throwing input. Restart program on error.
    try:
        amount_in_cents = int(input())
    except ValueError:
        print("You need to input an integer!")
        start()
        return

    # If the user's input is equal to or less than 0, inform them they will receive no change.
    # Return to escape function - don't run any further.
    if amount_in_cents <= 0:
        print("No change")
        return

    # Cast to int-type to prevent float values. Use division and modulus to accurately determine values.
    # Dollars = amount / 100
    # Quarters = Remainder of (amount / 100), divided by 25
    # Dimes = Remainder of the remainder of ((amount / 100) / 25)
    # ...
    dollars = int(amount_in_cents / 100)
    quarters = int((amount_in_cents % 100) / 25)
    dimes = int((amount_in_cents % 100 % 25) / 10)
    nickels = int((amount_in_cents % 100 % 25 % 10) / 5)
    pennies = int(amount_in_cents % 100 % 25 % 10 % 5)

    # Make a dictionary for storing the values.
    coin_purse = {}

    # Bunch of if-else statements to decide whether the keys of the coin_purse dict should be
    # plural or singular.
    if dollars == 1:
        coin_purse["Dollar"] = dollars
    else:
        coin_purse["Dollars"] = dollars

    if quarters == 1:
        coin_purse["Quarter"] = quarters
    else:
        coin_purse["Quarters"] = quarters

    if dimes == 1:
        coin_purse["Dime"] = dimes
    else:
        coin_purse["Dimes"] = dimes

    if nickels == 1:
        coin_purse["Nickel"] = nickels
    else:
        coin_purse["Nickels"] = nickels

    if pennies == 1:
        coin_purse["Penny"] = pennies
    else:
        coin_purse["Pennies"] = pennies

    # Cycle through the coin_purse dict to output the number of each currency.
    for currency in coin_purse:

        # Only output the number of that currency type if there is at least one of that currency.
        if coin_purse[currency] > 0:
            print(f"{coin_purse[currency]} {currency}")


# Run the start function.
start()