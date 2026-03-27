import json
import os
from modules.utils.colors import COLORS

NOTES_FILE = "./generated/notes.json"

def note_remove(*args):
    if not args:
        print("{COLORS['YELLOW']}Usage: note remove <title>{COLORS['RESET']}")
        return

    title_to_remove = " ".join(args).strip().lower()

    if not os.path.exists(NOTES_FILE):
        print("{COLORS['RED']}No notes found.{COLORS['RESET']}")
        return

    with open(NOTES_FILE, "r") as f:
        notes = json.load(f)

    updated_notes = [note for note in notes if note["title"].lower() != title_to_remove]

    if len(updated_notes) == len(notes):
        print(f"{COLORS['RED']}No note found with title: {title_to_remove}{COLORS['RESET']}")
        return

    with open(NOTES_FILE, "w") as f:
        json.dump(updated_notes, f, indent=4)

    print(f"{COLORS['GREEN']}Removed note: {title_to_remove}{COLORS['RESET']}")
