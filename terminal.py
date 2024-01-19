class Command:
    def __init__(self, name="", custom_function=None, description="", **kwargs):
        self.name = name
        self.description = description
        self.function = custom_function

        if custom_function is not None:
            self.arguments = self.get_function_arguments(custom_function)
        else:
            self.arguments = []

    def get_function_arguments(self, func):
        # Extract arguments from a function's code object
        arg_info = func.__code__
        if arg_info.co_varnames and arg_info.co_varnames[0] == 'self':
            # Skip 'self' for class methods
            return arg_info.co_varnames[1:arg_info.co_argcount]
        else:
            return arg_info.co_varnames[:arg_info.co_argcount]
            
        

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
            arguments = ""
            for arguement in self.commands[command].arguments:
                arguments =  arguments + " [" + arguement + "]"
            print(f'- {self.commands[command].name} {arguments} | {self.commands[command].description}')

    def execute_command(self, input_command, *args, **kwargs):
        if input_command in self.commands:
            command_obj = self.commands[input_command]
            if len(command_obj.function.__code__.co_varnames) == 0:
                command_obj.perform_function()
                return
            if command_obj.function.__code__.co_varnames[0] == 'self':  # Check if the first variable is 'self'
                expected_args = expected_args = command_obj.function.__code__.co_varnames[1:]  # Exclude 'self' for methods
            else:
                expected_args = expected_args = command_obj.function.__code__.co_varnames

            if len(args) < len(expected_args):
                print(f"Error: '{input_command}' expects {len(expected_args)} argument(s), got {len(args)}.")
                return

            command_obj.perform_function(*args[:len(expected_args)], **kwargs)
        else:
            print("Command not found!")

    def register_command(self, command_name, description, **kwargs):
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
        @self.register_command('exit', 'Exits the program.')
        def exit_program():
            exit()
        @self.register_command('clear', 'Clears the terminal.')
        def clear_terminal():
            print("\033c", end="")

        clear_terminal()
        print("Enter 'help' for a list of commands.")
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