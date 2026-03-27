import os
import json
from modules.utils.command_list import COMMAND_LIST

BASE_CONFIG_PATH = "./modules/generated/config"

def create_global_config():
    path = os.path.join(BASE_CONFIG_PATH, "global.json")
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({"use_password": False}, f, indent=4)
        print(f"Created: {path}")
    else:
        print(f"Exists: {path}")

def create_category_and_commands():
    for category, commands in COMMAND_LIST.items():
        category_name = category.replace(" ", "_").lower()
        category_path = os.path.join(BASE_CONFIG_PATH, category_name)
        os.makedirs(category_path, exist_ok=True)

        for command_name in commands.keys():
            file_name = command_name.replace(" ", "_").lower() + ".json"
            file_path = os.path.join(category_path, file_name)

            if not os.path.exists(file_path):
                default_config = {"enabled": True, "settings": {}}
                with open(file_path, "w") as f:
                    json.dump(default_config, f, indent=4)
                print(f"Created: {file_path}")
            else:
                print(f"Exists: {file_path}")

def config_init(*args):
    try:
        os.makedirs(BASE_CONFIG_PATH, exist_ok=True)
        create_global_config()
        create_category_and_commands()
        print("\nConfig initialization complete.")
    except Exception as e:
        print(f"Error: {e}")
