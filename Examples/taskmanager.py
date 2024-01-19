import terminal as terminalpkg

terminal = terminalpkg.CustomTerminal()

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"\nYour task '{str(task)}' has been added to your list.\n")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' has been removed from your list.")
        else:
            print(f"Task '{task}' has not been found. Try again later.")
    
    def list_tasks(self):
        if len(self.tasks) == 0:
            print("There are no tasks in your list.")
            return
        print("Tasks: ")
        for task in self.tasks:
            print(f'- {task}')

task_manager = TaskManager()
@terminal.register_command('add', 'Adds a task to your task list')
def add_task(task):
    task_manager.add_task(task)

@terminal.register_command('remove', 'Removes a task from your task list')
def remove_task(task):
    task_manager.remove_task(task)

@terminal.register_command('list', 'Lists all tasks')
def list_task():
    task_manager.list_tasks()

terminal.start()