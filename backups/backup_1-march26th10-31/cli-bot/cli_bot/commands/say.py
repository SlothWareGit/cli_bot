from utils import COLORS

def say_command():
    message = input(f"{COLORS['CYAN']}Enter a message to say: {COLORS['RESET']}")
    print(f"{COLORS['GREEN']}{message}{COLORS['RESET']}")