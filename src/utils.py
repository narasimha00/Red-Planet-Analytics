
# utils.py
import os

def clear():
    if os.sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
