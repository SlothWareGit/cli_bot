import json
import os
from modules.utils.colors import COLORS

NOTES_FILE = "./modules/generated/notes.json"

def note_add(*args):
    title = input(f"{COLORS['CYAN']}Title: {COLORS['RESET']}").strip()
    if not title:
        print(f"{COLORS['RED']}Title cannot be empty{COLORS['RESET']}")
        return

    content = input(f"{COLORS['CYAN']}Content: {COLORS['RESET']}").strip()
    if not content:
        print(f"{COLORS['RED']}Content cannot be empty{COLORS['RESET']}")
        return
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            json.dump([], f, indent=4)

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    note_id = len(notes) + 1

    notes.append({
        "id": note_id,
        "title": title,
        "content": content
    })
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

    print(f"{COLORS['GREEN']}Note added successfully!{COLORS['RESET']}")
