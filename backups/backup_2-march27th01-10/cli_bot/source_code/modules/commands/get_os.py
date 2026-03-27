import platform
from  modules.utils.colors import COLORS

def get_os():
    print(f"{COLORS['YELLOW']}Operating System:{COLORS['RESET']}{COLORS['CYAN']} {platform.system()}{COLORS['RESET']}")
    print(f"{COLORS['YELLOW']}OS Release:{COLORS['RESET']} {COLORS['CYAN']}{platform.release()}{COLORS['RESET']}")
    print(f"{COLORS['YELLOW']}Architecture:{COLORS['RESET']} {COLORS['CYAN']}{platform.machine()}{COLORS['RESET']}")
