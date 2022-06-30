# Establish and assign variables to user input. Convert to interger-type for future use.
age = int(input())
weight = int(input())
heart_rate = int(input())
time_elapsed = int(input())

# Establish and assign variable to math equation using interger-type variables.
calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * (time_elapsed / 8.368)

# Print output with a splice to show up to 2 decimal places.
print(f"Calories: {calories:.2f} calories")