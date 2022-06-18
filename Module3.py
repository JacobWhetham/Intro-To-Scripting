hours = 0

def calculate_hours(input_hours):
    regular_hours = input_hours

    # If we worked over 40 hours, we need to consider overtime.
    if regular_hours > 40:
        # Change the regular hours to 40, since that is our maximum.
        regular_hours = 40

        # The remaining hours is the amount of overtime.
        overtime_hours = input_hours - regular_hours

    # Hours * Payrate = Earned Amount. "//" is floor division, it rounds down to the nearest integer. We divide by a further 100 to get it rounded to 2 decimal places - dollars and cents.
        # e.g:
        # ((1.00 overtime_hour * 30) // 0.01) / 100)
        # (30.00 // .01) / 100
        # 3000.00 / 100
        # 30.00
    regular_pay = (regular_hours * 20.00 // 0.01) / 100
    overtime_pay = (overtime_hours * 30.00 // 0.01) / 100

    # Returns the hours and pay amounts.
    return regular_hours, overtime_hours, regular_pay, overtime_pay;

def start():
    print("How many hours did you work?")

    # Repeat if float is not given.
    try:
        # Allow partial hours by searching for a float.
        hours = float(input())
    except:
        print("Please enter an integer or float.")
        start()

    # Make a reference to the method to gather the returned info.
    calc = calculate_hours(hours)

    # Access the returned info as a list e.g. 'calc[0]'.
    print(f"You worked {hours} in total. Regular Hours: {calc[0]}. Overtime Hours: {calc[1]}. You should make ${calc[2] + calc[3]} in total. Regular Pay: ${calc[2]}. Overtime Pay: ${calc[3]}")




