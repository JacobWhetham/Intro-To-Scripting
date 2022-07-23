def swap_values(user_val1, user_val2):
    """Returns a tuple of the parameters in reverse order."""
    return user_val2, user_val1


if __name__ == '__main__':
    # Assign a tuple-type variable to the return of the swap_values function; use int-types of input for arguments.
    swapped_vals = swap_values(int(input()), int(input()))

    # Print out each value in swapped_vals while utilizing proper formatting.
    print(swapped_vals[0], end=' ')
    print(swapped_vals[1])