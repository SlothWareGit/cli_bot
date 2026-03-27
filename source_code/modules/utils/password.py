import os
import sys
import json
import bcrypt
import getpass

AUTH_FILE = "auth.json"

def authenticate_user():
    def create_password():
        print("{COLORS['RED']}No password found.{COLORS['RESET']} {COLORS['YELLOW']}Please create a password.{COLORS['RESET']}")
        while True:
            password = getpass.getpass("Create password:{COLORS['RESET']} ")
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("{COLORS['RED']}Passwords do not match. Try again.{COLORS['RESET']}")
            elif len(password) < 6:
                print("{COLORS['YELLOW']}Password too short. Minimum 6 characters.{COLORS['RESET']}")
            else:
                break
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        with open(AUTH_FILE, "w") as f:
            json.dump({"password_hash": hashed.decode()}, f)
        print("{COLORS['GREEN']}Password created successfully.{COLORS['RESET']}")

    def verify_password():
        with open(AUTH_FILE, "r") as f:
            data = json.load(f)
        stored_hash = data["password_hash"].encode()
        for attempt in range(3):
            password = getpass.getpass("{COLORS['CYAN']}Enter password:{COLORS['RESET']} ")
            if bcrypt.checkpw(password.encode(), stored_hash):
                print("{COLORS['GREEN']}Access granted.{COLORS['RESET']}")
                return
            else:
                print(f"{COLORS['YELLOW']}Incorrect password. {2 - attempt} attempts left.{COLORS['RESET']}")
        print("{COLORS['RED']}Too many failed attempts. Exiting.{COLORS['RESET']}")
        sys.exit()

    if not os.path.exists(AUTH_FILE):
        create_password()
    else:
        verify_password()
