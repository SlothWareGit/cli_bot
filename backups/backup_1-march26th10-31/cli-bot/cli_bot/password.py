import os
import sys
import json
import bcrypt
import getpass

AUTH_FILE = "auth.json"

def authenticate_user():
    def create_password():
        print("No password found. Please create a password.")
        while True:
            password = getpass.getpass("Create password: ")
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("Passwords do not match. Try again.")
            elif len(password) < 6:
                print("Password too short. Minimum 6 characters.")
            else:
                break
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        with open(AUTH_FILE, "w") as f:
            json.dump({"password_hash": hashed.decode()}, f)
        print("Password created successfully.")

    def verify_password():
        with open(AUTH_FILE, "r") as f:
            data = json.load(f)
        stored_hash = data["password_hash"].encode()
        for attempt in range(3):
            password = getpass.getpass("Enter password: ")
            if bcrypt.checkpw(password.encode(), stored_hash):
                print("Access granted.")
                return
            else:
                print(f"Incorrect password. {2 - attempt} attempts left.")
        print("Too many failed attempts. Exiting.")
        sys.exit()

    if not os.path.exists(AUTH_FILE):
        create_password()
    else:
        verify_password()
