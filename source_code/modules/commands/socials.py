from modules.utils.colors import COLORS

socials_links: dict[str, str] = {
    "Website": " https://slothwarehq.com/",
    "Discord": " link",
    "Email": " slothwarelabs@gmail.com",
    "Reddit": " link",
    "Github": " https://github.com/slothwaregit/",
    "YouTube": " https://youtube.com/@slothwarelabs",
    "Instagram": " link",
}

def socials():
    print(f"{COLORS['CYAN']}Socials:{COLORS['RESET']}\n")

    for cmd, desc in socials_links.items():
        print(
            f"{COLORS['YELLOW']}{cmd}{COLORS['RESET']}"
            f"{COLORS['CYAN']}{desc}{COLORS['RESET']}"
        )
