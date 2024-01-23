class Task:
    def __init__(self, task_id, description, due_date, status='Incomplete'):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.status = status


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = 'Complete'

    def display_tasks(self):
        for task in self.tasks:
            print(" ")
            print(f"Task {task.task_id}: {task.description} (Due: {task.due_date}, Status: {task.status})")
            print(" ")


class ToDoAppCLI:
    def __init__(self):
        self.todo_list = ToDoList()
        self.menu_options = {
            '1': self.add_task,
            '2': self.mark_complete,
            '3': self.display_tasks,
            '4': self.quit_app
        }

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-4): ")
            if choice in self.menu_options:
                self.menu_options[choice]()
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def print_menu(self):
        print("--------------------------")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Display Tasks")
        print("4. Quit")
        print("--------------------------")

    def add_task(self):
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        task = Task(len(self.todo_list.tasks) + 1, description, due_date)
        self.todo_list.add_task(task)

    def mark_complete(self):
        task_id = input("Enter task ID to mark as complete: ")
        self.todo_list.mark_complete(int(task_id))

    def display_tasks(self):
        self.todo_list.display_tasks()

    def quit_app(self):
        exit()


if __name__ == "__main__":
    app = ToDoAppCLI()
    app.run()
