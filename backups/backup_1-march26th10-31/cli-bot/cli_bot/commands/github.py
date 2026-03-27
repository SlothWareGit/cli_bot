import webbrowser
import subprocess
import platform
import os

def link_github():

    try:
        url = GITHUB_URL
    except NameError:
        url = "https://github.com/slothwaregit/cli_bot"

    try:
        if webbrowser.open(url):
            print("Opened GitHub in your default browser.")
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
        print("Opened GitHub in your default browser.")
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
        print("Could not open browser. Link copied to clipboard.")
        return
    except:
        pass

    print("Failed to open browser and could not copy to clipboard.")
