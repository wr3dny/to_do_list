def to_do(text):
    print(f"TO DO: {text}")


def options():
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")
    return choice


def main():
    options()
    match = {
        '1': 'add a task',
        '2': 'remove a task',
        '3': 'list all tasks',
        '4': 'exit'
    }
    print(f"You chose to {options()}")
    to_do('finish the script')


if __name__ == "__main__":
    main()
