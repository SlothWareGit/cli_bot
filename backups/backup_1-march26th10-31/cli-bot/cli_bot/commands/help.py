from utils import COLORS, COMMAND_LIST

def help_command():
    print(f"{COLORS['CYAN']}Available Commands:{COLORS['RESET']}\n")

    for cmd, desc in COMMAND_LIST.items():
        print(
            f"{COLORS['YELLOW']}{cmd}{COLORS['RESET']}: "
            f"{COLORS['WHITE']}{desc}{COLORS['RESET']}"
        )