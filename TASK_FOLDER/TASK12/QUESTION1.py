#Creating a to-do list
#Creating an empty list for the tasks
tasks = []


def add_task(task):
    while True:
        try:
            if task != "":
                print(f'{task} added successfully ')
            elif task.isdigit():
                print('Error, input a task')
            else:
                tasks.append(task)
        except ValueError:
            print("Try again")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")


def view_tasks():
    if tasks:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):  # Start numbering from 1
            print(f'{idx}. {task}')
    else:
        print("No tasks in your list!")


while True:
    try:
        print("\nOptions:" )
        print("1. Add Task")
        print("2. Remove task")
        print("3. View Task")
        print("4. Exit Program")

        

        # Ask user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter a task: ")
            add_task(task)
            
        elif choice == '2':
            task = input("Enter task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting program. Have a productive day!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
    except ValueError:
        print("Enter a number")