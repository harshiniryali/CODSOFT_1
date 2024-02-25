tasks = []

def your_tasks():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def add_a_task():
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
    print("Task added successfully!")

def remove_a_task():
    your_tasks()
    task_index = int(input("Enter the number of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Task removed successfully!")
    else:
        print("Invalid task number")

while True:
    print("\nTo-Do List Menu:")
    print("1. Show my tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        your_tasks()
    elif choice == '2':
        add_a_task()
    elif choice == '3':
        remove_a_task()
    elif choice == '4':
        break
    else:
        print("Invalid choice")