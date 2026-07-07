def show_menu():
    # Print the main menu options for the to-do list program.
    print("\nTo-Do List")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task complete")
    print("4. Remove task")
    print("5. Quit")


def list_tasks(tasks):
    # Display all tasks, with a checkmark for completed items.
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{index}. [{status}] {task['title']}")


def main():
    # Store the list of tasks in memory as a list of dictionaries.
    tasks = []

    # Keep the program running until the user chooses to quit.
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            # Add a new task with a title and default status of not done.
            title = input("Task title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                print(f"Added: {title}")
            else:
                print("Task title cannot be empty.")

        elif choice == "2":
            # Show the current list of tasks.
            list_tasks(tasks)

        elif choice == "3":
            # Mark a task as complete by selecting its number.
            list_tasks(tasks)
            number = input("Task number to complete: ").strip()
            if number.isdigit() and 1 <= int(number) <= len(tasks):
                tasks[int(number) - 1]["done"] = True
                print("Task marked complete.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            # Remove a task from the list by number.
            list_tasks(tasks)
            number = input("Task number to remove: ").strip()
            if number.isdigit() and 1 <= int(number) <= len(tasks):
                removed = tasks.pop(int(number) - 1)
                print(f"Removed: {removed['title']}")
            else:
                print("Invalid task number.")

        elif choice == "5":
            # Exit the program.
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices.
            print("Please choose a valid option.")


if __name__ == "__main__":
    # Start the to-do list program when this file is run directly.
    main()   