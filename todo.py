tasks = []

def add_task(task, priority="Medium"):
    entry = {"task": task, "priority": priority, "done": False}
    tasks.append(entry)
    print(f"Added: {task} (Priority: {priority})")

def remove_task(task):
    for entry in tasks:
        if entry["task"].lower() == task.lower():
            tasks.remove(entry)
            print(f"Removed: {task}")
            return
    print("Task not found!")

def mark_done(task):
    for entry in tasks:
        if entry["task"].lower() == task.lower():
            entry["done"] = True
            print(f"Marked as done: {task}")
            return
    print("Task not found!")

def search_task(keyword):
    results = [entry for entry in tasks if keyword.lower() in entry["task"].lower()]
    if results:
        print("\n--- Search Results ---")
        for i, entry in enumerate(results, 1):
            status = "✓" if entry["done"] else "✗"
            print(f"{i}. {entry['task']} [{entry['priority']}] {status}")
    else:
        print("No matching tasks found.")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n--- Tasks ---")
        for i, entry in enumerate(tasks, 1):
            status = "✓" if entry["done"] else "✗"
            print(f"{i}. {entry['task']} [{entry['priority']}] {status}")
        print(f"\nTotal: {len(tasks)} | Done: {sum(t['done'] for t in tasks)} | Pending: {len(tasks) - sum(t['done'] for t in tasks)}")

def main():
    while True:
        print("\n--- To-Do Menu ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. Show Tasks")
        print("5. Search Task")
        print("6. Exit")

        choice = input("Choose (1-6): ")

        if choice == "1":
            task = input("Enter task: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_task(task, priority.capitalize())

        elif choice == "2":
            task = input("Enter task to remove: ")
            remove_task(task)

        elif choice == "3":
            task = input("Enter task to mark done: ")
            mark_done(task)

        elif choice == "4":
            show_tasks()

        elif choice == "5":
            keyword = input("Enter keyword to search: ")
            search_task(keyword)

        elif choice == "6":
            print("Closing To-Do List. Bye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
