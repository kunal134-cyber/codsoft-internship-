todo_list = []

def show_menu():
    print("\n To-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print(" No tasks in the list.")
    else:
        print(" Your Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input(" Enter a new task: ")
    todo_list.append(task)
    print(f" Task added: {task}")

def remove_task():
    view_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input(" Enter the task number to remove: "))
        removed = todo_list.pop(task_num - 1)
        print(f" Task removed: {removed}")
    except (ValueError, IndexError):
        print(" Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print(" Exiting To-Do List. Have a productive day!")
            break
        else:
            print(" Invalid choice. Please select from 1 to 4.")

# Run the app
main()
