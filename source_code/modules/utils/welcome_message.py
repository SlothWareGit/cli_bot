import os
import platform
from modules.utils.colors import COLORS

GITHUB_URL = "https://github.com/slothwaregit/cli_bot"

def hyperlink(text: str, url: str) -> str:
    return f"\x1b]8;;{url}\x1b\\{text}\x1b]8;;\x1b\\"

def welcome_message():
    print(f"{COLORS['CYAN']}{'='*54}{COLORS['RESET']}")
    print(f"{COLORS['BLUE']}{' '*16}WELCOME TO THE CLI BOT      {COLORS['RESET']}")
    print(f"{COLORS['CYAN']}{'='*54}{COLORS['RESET']}\n")
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
