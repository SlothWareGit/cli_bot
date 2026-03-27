import time
import threading
import os
import sys

from modules.utils.command_callers import CALLERS_DICT
from modules.utils.colors import COLORS
from modules.utils.clear_screen import clear_screen
from modules.utils.welcome_message import welcome_message

try:
    import readline
    from readline import set_completer, parse_and_bind

    readline.set_completer_delims(' \t\n;')
    set_completer(lambda text, state: [
        cmd for cmd in CALLERS_DICT.keys() if cmd.startswith(text)
    ][state] if state < len([cmd for cmd in CALLERS_DICT.keys() if cmd.startswith(text)]) else None)
    parse_and_bind('tab: complete')

except ImportError:
    pass

def exit_command():
    print(f"{COLORS['YELLOW']}Exiting CLI...{COLORS['RESET']}")
    sys.exit()

clear_screen()
welcome_message()

def main():
    while True:
        try:
            user_input = input(f"{COLORS['MAGENTA']}𝔼𝕟𝕥𝕖𝕣 》》》 {COLORS['RESET']}").strip()
            if not user_input:
                continue

            command_key = user_input.lower()
            command_func = None
            args = []

            for key in CALLERS_DICT:
                if command_key.startswith(key):
                    command_func = CALLERS_DICT[key]
                    args = user_input[len(key):].strip().split()
                    break

            clear_screen()
            welcome_message()

            if not command_func:
                print(f"{COLORS['RED']}Unknown command: {user_input}{COLORS['RESET']}")
                continue

            try:
                command_func(*args)
            except TypeError:
                if args:
                    print(f"{COLORS['RED']}This command does not accept arguments{COLORS['RESET']}")
                else:
                    raise

        except KeyboardInterrupt:
            exit_command()
            break

if __name__ == "__main__":
    main()
