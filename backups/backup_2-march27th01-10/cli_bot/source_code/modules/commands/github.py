import webbrowser
import subprocess
import platform
import os
from modules.utils.colors import COLORS

def github():

    try:
        url = GITHUB_URL
    except NameError:
        url = "https://github.com/slothwaregit/cli_bot"

    try:
        if webbrowser.open(url):
            print("{COLORS['GREEN']}Opened GitHub in your default browser.{COLORS['RESET']}")
            return
    except:
        pass

    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(url)
        elif system == "Darwin":
            subprocess.run(["open", url])
        else:
            subprocess.run(["xdg-open", url])
        print("{COLORS['GREEN']}Opened GitHub in your default browser.{COLORS['RESET']}")
        return
    except:
        pass

    try:
        system = platform.system()
        if system == "Windows":
            subprocess.run("clip", input=url.encode(), check=True)
        elif system == "Darwin":
            subprocess.run("pbcopy", input=url.encode(), check=True)
        else:
            if "com.termux" in os.environ.get("PREFIX", ""):
                subprocess.run(["termux-clipboard-set"], input=url.encode(), check=True)
            else:
                subprocess.run(["xclip", "-selection", "clipboard"], input=url.encode(), check=True)
        print("{COLORS['RED']}Could not open browser.{COLORS['RESET']} {COLORS['YELLOW']}Link copied to clipboard.{COLORS['RESET']}")
        return
    except:
        pass

    print("{COLORS['RED']}Failed to open browser and could not copy to clipboard.{COLORS['RESET']}")
