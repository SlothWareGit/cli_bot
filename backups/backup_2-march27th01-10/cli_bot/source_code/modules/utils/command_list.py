from typing import Dict

COMMAND_LIST: Dict[str, Dict[str, str]] = {
    "General": {
        "help": "Shows this message",
        "clear": "Clears the console",
        "exit": "Exits the program",
        "refresh": "Refreshes the program (can apply code changed",
        "note add": "Add a idea/note",
        "note view": "View your notes/ideas",
        "note rm": "Remove a idea/note",
    },
    "Communication": {
        "say": "Makes the bot say something",
        "socials": "Displays socials and their links",
        "github": "Opens GitHub repo in default browser",
    },
    "Security": {
        "hash gen": "Generates a random or predetermined hash",
        "pswrd gen": "Generates a random password",
    },
    "System": {
        "get os": "Displays current OS, version, and Python version",
        "ip": "Displays IP info",
        "port scan": "Scans open ports",
        "port list": "Lists active ports",
    },
    "Settings": {
        "config init": "Creates config folders/files",
    }
}
