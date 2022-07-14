# Get the user's input.
user_text = input()

# Loop through the user's input.
for char in user_text:
    # If the element in the iteration is a space, period, or comma.
        # Note: .isalpha() cannot be used in this situation because it would eliminate other symbols, e.g. '!' or '$'.
    if char == ' ' or char == '.' or char == ',':
        # Update @user_text by reassigning it as itself with that character replaced.
        user_text = user_text.replace(char, "")

# Output the length user_text, after its modifications.
print(len(user_text))