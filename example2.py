import terminal

terminal = terminal.CustomTerminal()

@terminal.register_command('name', 'description')
def lmao(*args):
    print(*args)


terminal.start()