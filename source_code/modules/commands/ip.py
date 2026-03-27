import socket
import requests

def ip(args):
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        print(f"Hostname: {hostname}")
        print(f"Local IP: {local_ip}")

        if "--local" in args:
            return

        public_ip = requests.get("https://api.ipify.org").text
        print(f"Public IP: {public_ip}")

    except Exception as e:
        print(f"Error: {e}")
