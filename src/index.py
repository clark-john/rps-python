from rps_tui import cmd
from rps import play
from colorama import Fore, init, Style
from platform import system, python_version
from console_colors import consolecolor
from os import path

# This file is the starting point of the entire game.

init()
sys = system()
pyver = python_version()

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
	print("You're using",sys,"as of now.")
	print("Python Version:", pyver+consolecolor+bright)
	print("Wanna play? Type \'y\' to start the game or type \'n\' if you're exiting."+mag)
	print("Type \"cmds\" for special commands."+consolecolor)
	startup = input().lower()

	if startup == "y":
		play()
	elif startup == "n" or startup == 'exit':
		print("Exiting...")
		exit()
	elif startup == "cmds":
		cmd()
		break
	else:
		print(red+"Try again.\n")

# Version v1.0.6