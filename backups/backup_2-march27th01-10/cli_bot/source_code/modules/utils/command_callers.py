from typing import Dict
from modules.utils.refresh import refresh

from modules.commands.note_remove import note_remove
from modules.commands.note_add import note_add
from modules.commands.note_view import note_view
from modules.commands.clear_screen import clear_screen
from modules.commands.github import github
from modules.commands.help import help
from modules.commands.exit import exit
from modules.commands.pswrd_gen import pswrd_gen
from modules.commands.say import say
from modules.commands.sha256_hash_gen import hash_gen
from modules.commands.socials import socials
from modules.commands.get_os import get_os
from modules.commands.ip import ip
from modules.commands.port_scan import port_scan
from modules.commands.port_list import port_list
from modules.commands.config_init import config_init

CALLERS_DICT = {
    "help": help,
    "clear": clear_screen,
    "exit": exit,
    "refresh": refresh,
    "say": say,
    "socials": socials,
    "github": github,
    "hash gen": hash_gen,
    "pswrd gen": pswrd_gen,
    "get os": get_os,
    "ip": ip,
    "port scan": port_scan,
    "port list": port_list,
    "note add": note_add,
    "note rm": note_remove,
    "notes": note_view,
    "config init": config_init,
}
