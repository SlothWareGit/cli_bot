import json
import os
from modules.utils.colors import COLORS

NOTES_FILE = "./generated/notes.json"

def note_add(*args):
    title = input("{COLORS['CYAN']}Title: {COLORS['RESET']}").strip()
    if not title:
        print("{COLORS['RED']}Title cannot be empty{COLORS['RESET']}")
        return

    content = input("{COLORS['CYAN']}Content: {COLORS['RESET']}").strip()
    if not content:
        print("{COLORS['RED']}Content cannot be empty{COLORS['RESET']}")
        return

    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            notes = json.load(f)
    else:
        notes = []

    note = {
        "title": title,
        "content": content
    }

    notes.append(note)

    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

    print("Note saved.")
