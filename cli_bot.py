import os
import hashlib
import sys
import random
import string
import secrets
import readline
import time

readline.parse_and_bind("tab: complete")

COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m"
}


COMMAND = {
    f"{COLORS['YELLOW']}help{COLORS['RESET']}": f"{COLORS['WHITE']}shows this message{COLORS['RESET']}",
    f"{COLORS['YELLOW']}clear{COLORS['RESET']}": f"{COLORS['WHITE']}clears the console{COLORS['RESET']}",
    f"{COLORS['YELLOW']}say{COLORS['RESET']}": f"{COLORS['WHITE']}makes the bot say something (usage: say [message]){COLORS['RESET']}",
    f"{COLORS['YELLOW']}generate{COLORS['RESET']}": f"{COLORS['WHITE']}generates a random sha256 encryption{COLORS['RESET']}",
    f"{COLORS['YELLOW']}refresh{COLORS['RESET']}": f"{COLORS['WHITE']}refreshes the program to apply code changes{COLORS['RESET']}",
    f"{COLORS['YELLOW']}pswrd-gen{COLORS['RESET']}": f"{COLORS['WHITE']}generates a random password with letters, digits, and special characters{COLORS['RESET']}",
    f"{COLORS['YELLOW']}exit{COLORS['RESET']}": f"{COLORS['WHITE']}exits the program{COLORS['RESET']}"
}

def welcome_message(): 
    print(f"{COLORS['CYAN']}{'='*40}{COLORS['RESET']}")
    print(f"{COLORS['BLUE']}      WELCOME TO THE CLI BOT      {COLORS['RESET']}")
    print(f"{COLORS['CYAN']}{'='*40}{COLORS['RESET']}\n")
    print(f"{COLORS['WHITE']}Type {COLORS['YELLOW']}help{COLORS['WHITE']} to see a list of commands.{COLORS['RESET']}")
    print(f"{COLORS['WHITE']}This bot is open source on GitHub: {COLORS['CYAN']}https://github.com/slothwaregit/cli_bot{COLORS['RESET']}\n")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
welcome_message()

try:
    while True:
        usrinp = input(f"{COLORS['MAGENTA']}Enter Command >>> {COLORS['RESET']}")

        if usrinp == "help":
            print(f"{COLORS['CYAN']}Available commands:{COLORS['RESET']}\n"
                + "\n".join(f"{cmd}: {desc}" for cmd, desc in COMMAND.items()))
        
        elif usrinp == "clear" :
            clear_screen()
            welcome_message()
        
        elif usrinp.startswith("say ") :
            message = usrinp[4:]  # Extract the message after "/say " ; 4 is the length of "/say " so it skips that part
            print(f"{COLORS['WHITE']}{message}{COLORS['RESET']}")

        elif usrinp == "generate" :
            usrinp4 = input(f"{COLORS['CYAN']}Enter a seed (or leave blank for random): {COLORS['RESET']}")
            if usrinp4:
                    astring = usrinp4
            else:
                astring: str = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        
            sha256_hash = hashlib.sha256(astring.encode()).hexdigest()
        
            print(f"{COLORS['WHITE']}Random String: {astring}{COLORS['RESET']}")
            print(f"{COLORS['WHITE']}SHA256 Hash: {sha256_hash}{COLORS['RESET']}")

        elif usrinp == "refresh" :
            os.execv(sys.executable, [sys.executable] + sys.argv)

        elif usrinp == "pswrd-gen":

            while True:
                try:
                    usrinp2 = int(input(f"{COLORS['CYAN']}Enter minimum password length (8): {COLORS['RESET']}"))
                    if usrinp2 < 8:
                        print(f"{COLORS['YELLOW']}Minimum must be at least 8.{COLORS['RESET']}")
                        continue
                    break
                except ValueError:
                    print(f"{COLORS['RED']}Enter a valid number.{COLORS['RESET']}")

            while True:
                try:
                    usrinp3 = int(input(f"{COLORS['CYAN']}Enter maximum password length: {COLORS['RESET']}"))
                    if usrinp3 < usrinp2:
                        print(f"{COLORS['YELLOW']}Max must be greater than or equal to min.{COLORS['RESET']}")
                        continue
                    break
                except ValueError:
                    print(f"{COLORS['RED']}Enter a valid number.{COLORS['RESET']}")

            length = random.randint(usrinp2, usrinp3)

            lowercase = "abcdefghijkmnopqrstuvwxyz"
            uppercase = "ABCDEFGHJKLMNPQRSTUVWXYZ"
            digits = "123456789"
            symbols = "!@#$%^&*()-_=+[]{};:,.<>?"

            all_chars = lowercase + uppercase + digits + symbols

            password = [
                secrets.choice(lowercase),
                secrets.choice(uppercase),
                secrets.choice(digits),
                secrets.choice(symbols)
            ]

            password += [secrets.choice(all_chars) for _ in range(length - 4)]

            secrets.SystemRandom().shuffle(password)

            password = ''.join(password)

            print(f"{COLORS['GREEN']}Generated Password:{COLORS['RESET']} {COLORS['WHITE']}{password}{COLORS['RESET']}")

        elif usrinp == "exit" :
            print(f"{COLORS['BLUE']}Goodbye!{COLORS['RESET']}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        else :  
            print(f"{COLORS['RED']}Unknown command, use{COLORS['RESET']} {COLORS['YELLOW']}help{COLORS['RESET']} {COLORS['RED']}if you need help{COLORS['RESET']}")
except KeyboardInterrupt:
    print(f"\n{COLORS['BLUE']}Goodbye!{COLORS['RESET']}")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    exit()