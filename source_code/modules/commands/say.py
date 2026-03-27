from modules.utils.colors import COLORS

def say():
    message = input(f"{COLORS['CYAN']}Enter a message to say: {COLORS['RESET']}")
    print(f"{COLORS['GREEN']}{message}{COLORS['RESET']}")
