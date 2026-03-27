from modules.utils.command_list import COMMAND_LIST
from modules.utils.colors import COLORS

def help():
    for category, cmds in COMMAND_LIST.items():
        print(f"\n{COLORS['GREEN']}=== {category} ==={COLORS['RESET']}")
        for cmd, desc in cmds.items():
            print(f"{COLORS['CYAN']}{cmd}{COLORS['RESET']}: {COLORS['YELLOW']}{desc}{COLORS['RESET']}")


