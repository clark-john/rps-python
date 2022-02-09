from commands import cmd
from sys import exit
from rps import play

# This file is the starting point of the entire game.

while True:
    startup = input("Wanna play rock, paper, and scissors? (y/n)\nType \"cmds\" for special commands.\n").lower()
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
        print("Try again.")


# Version v1.0.1