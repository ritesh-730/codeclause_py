tasks = []

def create_task():
    task = input("Enter a task: ")
    tasks.append({"task": task, "status": "pending"})
    print(f"Task '{task}' created!")

def view_tasks():
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']}")

def track_tasks():
    print("Your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['task']} - {task['status']}")

def update_task():
    task_name = input("Enter the task to update: ")
    for task in tasks:
        if task["task"] == task_name:
            new_status = input("Enter the new status (pending/completed): ")
            task["task"] = task_name
            task["status"] = new_status
            print("Task updated!")
            return
    print("Task not found!")

def delete_task():
    task_name = input("Enter the task to delete: ")
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)
            print("Task deleted!")
            return
    print("Task not found!")    

while True:
    print("To-Do List App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Track tasks")
    print("4. Update")
    print("5. Delete task")
    print("6. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        create_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        track_tasks()
    elif choice == "4":
        update_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again!")







