import random
import secrets
from utils import COLORS

def password_gen_command():
    while True:
        try:
            min_len = int(input(f"{COLORS['CYAN']}Enter minimum password length (8): {COLORS['RESET']}"))
            if min_len < 8:
                print(f"{COLORS['YELLOW']}Minimum must be at least 8.{COLORS['RESET']}")
                continue
            break
        except ValueError:
            print(f"{COLORS['RED']}Enter a valid number.{COLORS['RESET']}")

    while True:
        try:
            max_len = int(input(f"{COLORS['CYAN']}Enter maximum password length: {COLORS['RESET']}"))
            if max_len < min_len:
                print(f"{COLORS['YELLOW']}Max must be greater than or equal to min.{COLORS['RESET']}")
                continue
            break
        except ValueError:
            print(f"{COLORS['RED']}Enter a valid number.{COLORS['RESET']}")

    length = random.randint(min_len, max_len)

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