from modules.utils.clear_screen import clear_screen
from modules.utils.colors import COLORS
import sys

def exit():
    print(f"{COLORS['CYAN']}Goodbye!{COLORS['RESET']}")
    clear_screen()
    sys.exit()
