import os

def clear_screen():
    # Check the platform and execute the appropriate command
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # 'posix' stands for Linux, macOS, etc.
        os.system('clear')

