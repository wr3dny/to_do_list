import json


def to_do(text):
    print(f"TO DO: {text}")


def read_file():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
    return tasks


def new_task():
    task_name = input("Enter the task name: ")
    task_description = input("Enter the task description: ")
    task_deadline = input("Enter the task deadline: ")
    return task_name, task_description, task_deadline


def write_file(task_name, task_description, task_deadline):
    with open('tasks.txt', 'a') as file:
        task_dict = {
            "name": task_name,
            "description": task_description,
            "deadline": task_deadline
        }
        json.dump(task_dict, file)
        file.write('\n')

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




def options(choice):
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
