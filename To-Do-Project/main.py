tasks = []


def add_task():
    task_desc = input("Enter the task description: ")
    task = {"description": task_desc, "completed": False}
    tasks.append(task)
    print(f'Task {task_desc} added')


def view_tasks():
    if not tasks:
        print("No Tasks Added")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task['completed'] else 'Not Done'
            print(f"{idx}. {task['description']} - {status}")


def mark_task_done():
    view_tasks()
    task_num = int(input("Enter the task number to mark as done: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print(f'Task "{tasks[task_num - 1]["description"]}" marked as done.')
    else:
        print("Invalid task number!")


def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f'Task "{removed_task["description"]}" deleted.')
    else:
        print("Invalid task number!")


def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
