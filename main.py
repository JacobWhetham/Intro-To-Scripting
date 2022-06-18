# Allow access to other Python files in project.
import Module2, Module3, Module4, Module5

# Add the Python files to a list.
modules = [Module2, Module3, Module4, Module5]


def start():
    print("Enter the number for the file do you want to run, or 'exit' to quit.")
    i = 1

    # For every Python file in the list:
    for each in modules:
        # "Selection Number. String-version of the Python File Name."
        print(f"{i}. {str(modules[i-1])}")

        # Next selection number.
        i += 1

    # Allow for user selection.
    answer = input()

    if answer == 'exit':
        quit()

    try:
        # Run the start() method in the selected Python file.
        modules[int(answer)-1].start()
    except:
        print("Please either enter 'exit' or an integer.")
        start()

    # For cleanliness in the console.
    print("---------------------------------------------------")
    start()


if __name__ == '__main__':
    start()