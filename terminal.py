class Command:
    def __init__(self, name="", custom_function=None, description=""):
        self.name = name
        self.description = description
        self.function = custom_function

    def perform_function(self, *args, **kwargs):
        if self.function:
            self.function(*args, **kwargs)

class CustomTerminal:
    def __init__(self):
        self.commands = {}
        self.command_line_prompt = "<root> $ "

    def show_commands(self):
        print("Help menu:")
        for command in self.commands:
            print(f'- {self.commands[command].name} | {self.commands[command].description}')

    def execute_command(self, input_command, *args, **kwargs):
        if input_command in self.commands:
            command_obj = self.commands[input_command]
            expected_args = len(command_obj.function.__code__.co_varnames[1:])  # Exclude 'self' for methods
            if expected_args == 0:
                command_obj.perform_function()
                return

            if len(args) < expected_args:
                print(f"Error: '{input_command}' expects {expected_args} arguments, got {len(args)}.")
                return

            command_obj.perform_function(*args[:expected_args], **kwargs)
        else:
            print("Command not found!")

    def register_command(self, command_name, description):
        def decorator(func):
            command = Command(command_name, func, description)
            self.commands[command_name] = command

            # Optionally, you can return a wrapped function
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def start(self):
        @self.register_command('help', 'Shows this menu.')
        def show_commands():
            self.show_commands()

        @self.register_command('sum', 'Sums two numbers.')
        def sum_numbers(a, b):
            try:
                result = int(a) + int(b)
                print(f"The sum of {a} and {b} is: {result}")
            except ValueError:
                print("Invalid arguments! No numbers! >:(")

        while True:
            user_input = input(self.command_line_prompt)
            command = user_input.split(" ")[0]
            arguments = user_input.split(" ")[1:]
            self.execute_command(command, *arguments)


if __name__ == "__main__":
    global terminal_instance
    terminal_instance = CustomTerminal()


def main():
    # Register the 'help' command
    @terminal_instance.register_command('help', 'Shows this menu')
    def show_commands():
        terminal_instance.show_commands()

    # Execute the 'sum' command with arguments

    terminal_instance.start()


if __name__ == "__main__":
    main()
