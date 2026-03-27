import hashlib
import random
import string
from modules.utils.colors import COLORS

def hash_gen():
    seed_input = input(f"{COLORS['CYAN']}Enter a seed (or leave blank for random): {COLORS['RESET']}").strip()
    
    if seed_input:
        astring = seed_input
    else:
        astring = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    sha256_hash = hashlib.sha256(astring.encode()).hexdigest()

    print(f"{COLORS['WHITE']}Random String: {astring}{COLORS['RESET']}")
    print(f"{COLORS['WHITE']}SHA256 Hash: {sha256_hash}{COLORS['RESET']}")
