import os
from modules.utils.colors import COLORS

def port_list(args):
    try:
        os.system("netstat -tulnp")
    except:
        print("{COLORS['RED']}netstat not available on this system{COLORS['RESET']}")
