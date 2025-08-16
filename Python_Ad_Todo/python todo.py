# -------------------------------------------------------
# To-Do List Application
# Project Code: JKUAD0910
# -------------------------------------------------------

class Task:
    """Class representing a task in To-Do List [JKUAD0910]"""
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✔ Completed" if self.completed else "✘ Pending"
        return f"{self.description} [{status}]"


class ToDoList:
    """To-Do List Manager [JKUAD0910]"""
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully! [JKUAD0910]")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task '{self.tasks[index].description}' marked as completed. [JKUAD0910]")
        else:
            print("Invalid task number. [JKUAD0910]")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available. [JKUAD0910]")
        else:
            print("\nYour To-Do List [JKUAD0910]:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")


def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu --- [JKUAD0910]")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Enter task description: ")
            todo.add_task(desc)

        elif choice == "2":
            todo.view_tasks()
            num = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_task_completed(num)

        elif choice == "3":
            todo.view_tasks()

        elif choice == "4":
            print("Exiting To-Do List App. Goodbye! [JKUAD0910]")
            break

        else:
            print("Invalid choice. Please try again. [JKUAD0910]")


if __name__ == "__main__":
    main()
