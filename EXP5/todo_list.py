tasks = []

while True:
    print("\n1.Add Task 2.View Tasks 3.Remove Task 4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == 2:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == 3:
        t = int(input("Enter task number to remove: "))
        if 0 < t <= len(tasks):
            tasks.pop(t - 1)

    elif choice == 4:
        break
