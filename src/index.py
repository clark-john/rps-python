from rps_cli import cmd
from sys import exit
from rps import play
from colorama import Fore, init, Style
from platform import system
from configparser import ConfigParser
from console_colors import consolecolor

# This file is the starting point of the entire game.

config = ConfigParser()
config.read('./settings.ini')
init()
sys = system()

# Colorama Variables

bright = Style.BRIGHT
green = Fore.GREEN + bright
reset = Fore.RESET
mag = Fore.MAGENTA + bright
yel = Fore.YELLOW + bright
red = Fore.RED

# Main Startup

while True:
    print(green+"Welcome to rps-python!\n"+yel)
    print("You're using",sys,"as of now."+consolecolor)
    print("Wanna play? Type \'y\' to start the game or type \'n\' if you're exiting."+mag)
    print("Type \"cmds\" for special commands."+consolecolor)
    startup = input().lower()

    if startup == "y":
        play()
        break
    elif startup == "n" or startup == 'exit':
        print("Exiting...")
        exit()
    elif startup == "cmds":
        cmd()
        break
    else:
        print(red+"Try again.\n")

# Version v1.0.2