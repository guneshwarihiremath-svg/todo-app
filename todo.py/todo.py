# todo.py
tasks = []   # store tasks in a list

def show_tasks():
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")

def remove_task(index):
    if 0 < index <= len(tasks):
        removed = tasks.pop(index-1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number!")

while True:
    print("\n1. Show Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task(input("Enter task: "))
    elif choice == "3":
        remove_task(int(input("Enter task number: ")))
    elif choice == "4":
        break
    else:
        print("❌ Invalid choice!")