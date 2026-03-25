import os
import sys
import utils
from utils import COLORS, clear_screen
from commands.github import link_github
from commands.help import help_command
from commands.exit import exit_command
from commands.pswrd_gen import password_gen_command
from commands.say import say_command
from commands.sha256_hash_gen import hash_gen 

try:
    import readline 
    from readline import set_completer, parse_and_bind

    readline.set_completer_delims(' \t\n;')
    set_completer(lambda text, state: [cmd for cmd in utils.COMMAND_LIST if cmd.startswith(text)][state] if state < len([cmd for cmd in utils.COMMAND_LIST if cmd.startswith(text)]) else None)
    parse_and_bind('tab: complete')

except ImportError:
    pass

def main():
    clear_screen()
    utils.welcome_message()
    while True:
        user_input = input(f"{COLORS['MAGENTA']}Enter Command >>> {COLORS['RESET']}")
        command_parts = user_input.strip().split()
        if not command_parts:
            continue
        command = command_parts[0].lower()
        args = command_parts[1:]

        if command == "help":
            clear_screen()
            utils.welcome_message()
            help_command()
        elif command == "clear":
            clear_screen()
            utils.welcome_message()
        elif command == "pswrd-gen":
            clear_screen()
            utils.welcome_message()
            password_gen_command()
        elif command == "hash-gen":
            clear_screen()
            utils.welcome_message()
            hash_gen()
        elif command == "say":
            clear_screen()
            utils.welcome_message()
            say_command()
        elif command == "github":
            clear_screen()
            utils.welcome_message()
            link_github()
        elif command == "refresh":
            os.execv(sys.executable, [sys.executable] + sys.argv)
        elif command == "exit":
            exit_command()
        else:
            print(f"{COLORS['RED']}Unknown command: {command}{COLORS['RESET']}")

try:
    main()
except KeyboardInterrupt:
    exit_command()  
if __name__ == "__main__":
    main()
