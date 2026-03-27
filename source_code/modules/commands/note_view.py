import json
import os
from modules.utils.colors import COLORS

NOTES_FILE = "./modules/generated/notes.json"

def note_view(*args):
    if not os.path.exists(NOTES_FILE):
        print("{COLORS['RED']}No notes found.{COLORS['RESET']}")
        return

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    if not notes:
        print("{COLORS['RED']}No notes found.{COLORS['RESET']}")
        return

    for i, note in enumerate(notes, start=1):
        print(f"{COLORS['CYAN']}{i}. {note['title']}{COLORS['RESET']}")
        print(f"{COLORS['CYAN']}   - {note['content']}{COLORS['RESET']}")
