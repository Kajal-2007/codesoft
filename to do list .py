

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            for index, task in enumerate(self.tasks, 1):
                status = "Done" if task["completed"] else "Not completed"
                print(f"{index}. {task['task']} - {status}")

    def mark_completed(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        except IndexError:
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
