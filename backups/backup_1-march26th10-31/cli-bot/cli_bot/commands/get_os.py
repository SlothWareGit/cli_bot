import platform

def get_os():
    print(f"Operating System: {platform.system()}")
    print(f"OS Release: {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Python Version: {platform.python_version()}")
