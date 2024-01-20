class Command:
    def __init__(self, name="", custom_function=None, description="", **kwargs):
        # Initialize Command object with provided attributes
        self.name = name
        self.description = description
        self.function = custom_function

        # Determine function arguments, default to an empty list if no function provided
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
        # Execute the function if available
        if self.function:
            self.function(*args, **kwargs)

class CustomTerminal:
    def __init__(self):
        # Initialize CustomTerminal object with an empty dictionary for commands
        self.commands = {}
        self.command_line_prompt = "<root> $ "

    def show_commands(self):
        # Display the help menu with command names, arguments, and descriptions
        print("Help menu:")
        for command in self.commands:
            arguments = ""
            for argument in self.commands[command].arguments:
                arguments =  arguments + " [" + argument + "]"
            print(f'- {self.commands[command].name} {arguments} | {self.commands[command].description}')
    def parse_arguments(self, input_string):
        # Split the input string into a list of words
        words = input_string.split()

        # Combine words enclosed in double quotes
        combined_args = []
        current_arg = ""

        for word in words:
            if word.startswith('"'):
                # Start of a quoted argument
                current_arg = word[1:]
            elif word.endswith('"'):
                # End of a quoted argument
                current_arg += " " + word[:-1]
                combined_args.append(current_arg)
                current_arg = ""
            else:
                # Regular word
                combined_args.append(word)
        print(combined_args)
        return combined_args
    def execute_command(self, input_command, argument_strings):
        # Execute the command if available
        if input_command in self.commands:
            command_obj = self.commands[input_command]
            args = self.parse_arguments(argument_strings)
            # Determine expected arguments based on the function's code object
            if len(command_obj.function.__code__.co_varnames) == 0:
                command_obj.perform_function()
                return
            if command_obj.function.__code__.co_varnames[0] == 'self':
                expected_args = command_obj.function.__code__.co_varnames[1:]
            else:
                expected_args = command_obj.function.__code__.co_varnames

            # Check if the correct number of arguments are provided
            if len(args) < len(expected_args):
                print(f"Error: '{input_command}' expects {len(expected_args)} argument(s), got {len(args)}.")
                return

            # Execute the command with the provided arguments
            command_obj.perform_function(*args[:len(expected_args)])
        else:
            print("Command not found!")

    def register_command(self, command_name, description, **kwargs):
        # Decorator function to register a new command
        def decorator(func):
            # Create a Command object and add it to the commands dictionary
            command = Command(command_name, func, description)
            self.commands[command_name] = command

            # Optionally, you can return a wrapped function
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def start(self):
        # Register built-in commands and display initial information
        @self.register_command('help', 'Shows this menu')
        def show_commands():
            self.show_commands()
        @self.register_command('exit', 'Exits the program.')
        def exit_program():
            clear_terminal()
            print("Exiting terminal, bye bye!\n")
            exit()
        @self.register_command('clear', 'Clears the terminal.')
        def clear_terminal():
            print("\033c", end="")

        clear_terminal()
        print("Enter 'help' for a list of commands.")
        while True:
            # Accept user input, extract command and arguments, and execute the command
            user_input = input(self.command_line_prompt)
            command = user_input.split(" ")[0]
            arguments = " ".join(user_input.split(" ")[1:])
            self.execute_command(command, arguments)

if __name__ == "__main__":
    # Create a global terminal_instance for external use
    global terminal_instance
    terminal_instance = CustomTerminal()

def main():
    # Register the 'help' command and start the terminal
    @terminal_instance.register_command('help', 'Shows this menu')
    def show_commands():
        terminal_instance.show_commands()

    # Execute the 'sum' command with arguments
    terminal_instance.start()

if __name__ == "__main__":
    main()
