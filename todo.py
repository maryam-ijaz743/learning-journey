tasks = []

while True:
    print("\n--- TODO LIST ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks added yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, task)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
