undo_stack = []
redo_stack = []
limit = 10  

def do_action(action):
    if len(undo_stack) >= limit:
        undo_stack.pop(0)  
    undo_stack.append(action)
    redo_stack.clear()
    print(f"Action done: {action}")

def undo_action():
    if undo_stack:
        last = undo_stack.pop()
        redo_stack.append(last)
        print(f"Undo: {last}")
    else:
        print("Nothing to undo!")

def redo_action():
    if redo_stack:
        last = redo_stack.pop()
        undo_stack.append(last)
        print(f"Redo: {last}")
    else:
        print("Nothing to redo!")

def undo_all():
    if undo_stack:
        while undo_stack:
            last = undo_stack.pop()
            redo_stack.append(last)
        print("All actions undone!")
    else:
        print("Nothing to undo!")

def redo_all():
    if redo_stack:
        while redo_stack:
            last = redo_stack.pop()
            undo_stack.append(last)
        print("All actions redone!")
    else:
        print("Nothing to redo!")

def show_history():
    print("\n--- History ---")
    if not undo_stack:
        print("No actions yet.")
    else:
        for i, act in enumerate(undo_stack, 1):
            print(f"{i}. {act}")

def main():
    while True:
        print("\n--- Undo/Redo Menu ---")
        print("1. Do Action")
        print("2. Undo Last Action")
        print("3. Redo Last Action")
        print("4. Undo All")
        print("5. Redo All")
        print("6. Show History")
        print("7. Exit")

        choice = input("Choose (1-7): ")

        if choice == "1":
            action = input("Enter action: ")
            do_action(action)

        elif choice == "2":
            undo_action()

        elif choice == "3":
            redo_action()

        elif choice == "4":
            undo_all()

        elif choice == "5":
            redo_all()

        elif choice == "6":
            show_history()

        elif choice == "7":
            print("Closing Undo/Redo. Bye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
