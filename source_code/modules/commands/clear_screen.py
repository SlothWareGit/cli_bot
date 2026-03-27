import os
from modules.utils.welcome_message import welcome_message

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome_message()
