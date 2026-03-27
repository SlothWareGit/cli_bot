import os
import sys

def refresh():
    os.execv(sys.executable, [sys.executable] + sys.argv)
