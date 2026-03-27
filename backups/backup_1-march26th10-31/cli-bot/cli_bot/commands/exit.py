from utils import COLORS, clear_screen

def exit_command():
    print(f"{COLORS['CYAN']}Goodbye!{COLORS['RESET']}")
    clear_screen()
    exit()