import os

COLORS: dict[str, str] = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m"
}

COMMAND_LIST: dict[str, str] = {
    "help": "shows this message",
    "clear": "clears the console",
    "say": "makes the bot say something",
    "hash-gen": "generates a random or predetermined sha256 encryption",
    "refresh": "refreshes the program",
    "pswrd-gen": "generates a random password",
    "exit": "exits the program"
}

def welcome_message(): 
    print(f"{COLORS['CYAN']}{'='*40}{COLORS['RESET']}")
    print(f"{COLORS['BLUE']}      WELCOME TO THE CLI BOT      {COLORS['RESET']}")
    print(f"{COLORS['CYAN']}{'='*40}{COLORS['RESET']}\n")
    print(f"{COLORS['WHITE']}Type {COLORS['YELLOW']}help{COLORS['WHITE']} to see a list of commands.{COLORS['RESET']}")
    print(f"{COLORS['WHITE']}This bot is open source on GitHub: {COLORS['CYAN']}https://github.com/slothwaregit/cli_bot{COLORS['RESET']}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
