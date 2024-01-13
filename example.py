import terminal

terminal = terminal.CustomTerminal()

class TaskManager():
    def __init__(self):
        self.tasks = []

    @terminal.register_command('add', 'add_task')
    def add_task(self, task):
        self.tasks.append(task)
        print(f"\nYour task '{task}' has been added to your list.\n")
    
    @terminal.register_command('remove', 'Removes a task from the list')
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' has been removed from your list.")
        else:
            print(f"Task '{task}' has not been found. Try again later.")
    
    @terminal.register_command('list', 'Lists all tasks')
    def list_tasks(self):
        print("Tasks: ")
        for task in self.tasks:
            print(f'- {task}')
    
terminal.start()