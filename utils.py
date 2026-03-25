import os
import platform

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
    "github": "opens github repo in default browser",
    "refresh": "refreshes the program",
    "pswrd-gen": "generates a random password",
    "exit": "exits the program"
}

GITHUB_URL = "https://github.com/slothwaregit/cli_bot"

def hyperlink(text: str, url: str) -> str:
    return f"\x1b]8;;{url}\x1b\\{text}\x1b]8;;\x1b\\"

def welcome_message(): 
    print(f"{COLORS['CYAN']}{'='*40}{COLORS['RESET']}")
    print(f"{COLORS['BLUE']}      WELCOME TO THE CLI BOT      {COLORS['RESET']}")
    print(f"{COLORS['CYAN']}{'='*40}{COLORS['RESET']}\n")
    print(f"{COLORS['WHITE']}Type {COLORS['YELLOW']}help{COLORS['WHITE']} to see a list of commands.{COLORS['RESET']}")

    if platform.system() == "Windows":
        link = hyperlink("GitHub Repo", GITHUB_URL)
        print(f"{COLORS['WHITE']}This bot is open source on GitHub: {COLORS['CYAN']}{link}{COLORS['RESET']}\n")
    else:
        print(f"{COLORS['WHITE']}This bot is open source on GitHub: {COLORS['CYAN']}{GITHUB_URL}{COLORS['RESET']}\n")

    if platform.system() == "Windows":
        print(f"{COLORS['YELLOW']}Note: You may encounter some bugs or limitations on Windows.{COLORS['RESET']}\n")
    else:
        print(f"{COLORS['YELLOW']}Note: This bot is optimized for Unix-like systems.{COLORS['RESET']}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
