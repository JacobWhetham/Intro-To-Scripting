def exact_change(user_total):
    """Converts and returns the input into the fewest coins and dollars"""

    # Output an error if the amount is invalid and exit the function early by returning a tuple of five zeroes.
    if user_total <= 0:
        print("no change")
        return 0, 0, 0, 0, 0

    # Get the number of each currency and update user_total accordingly.
    dollars = int(user_total / 100)
    user_total -= dollars * 100

    quarters = int(user_total / 25)
    user_total -= quarters * 25

    dimes = int(user_total / 10)
    user_total -= dimes * 10

    nickels = int(user_total / 5)
    user_total -= nickels * 5

    pennies = user_total

    # Return a tuple of the amounts of each currency denomination.
    return dollars, quarters, dimes, nickels, pennies


# The default run condition.
if __name__ == '__main__':
    # Get user's input and set a tuple equal to the return of the exact_change function.
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Determine the proper output based on the amount of each currency - excluded, singular, or plural.
    if num_dollars == 0:
        pass
    elif num_dollars == 1:
        print(num_dollars, 'dollar')
    else:
        print(num_dollars, 'dollars')

    if num_quarters == 0:
        pass
    elif num_quarters == 1:
        print(num_quarters, 'quarter')
    else:
        print(num_quarters, 'quarters')

    if num_dimes == 0:
        pass
    elif num_dimes == 1:
        print(num_dimes, 'dime')
    else:
        print(num_dimes, 'dimes')

    if num_nickels == 0:
        pass
    elif num_nickels == 1:
        print(num_nickels, 'nickel')
    else:
        print(num_nickels, 'nickels')

    if num_pennies == 0:
        pass
    elif num_pennies == 1:
        print(num_pennies, 'penny')
    else:
        print(num_pennies, 'pennies')