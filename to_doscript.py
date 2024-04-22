import json


def to_do(text):
    print(f"TO DO: {text}")


def read_file():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
    return tasks


def task_name():
    task = input("Enter the task name: ")
    return task


def write_file(task):
    with open('tasks.txt', 'a') as file:
        json.dump(task, file)
        file.write(task + '\n')

def menu():
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")
    while choice not in ['1', '2', '3', '4']:
        print("Invalid choice")
        choice = input("Enter your choice: ")
    return choice




def options():
    print("1. Add a task")
    print("2. Remove a task")
    print("3. List all tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")
    return choice


def main():
    print(read_file())
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
