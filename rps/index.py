import commands
import sys
import rps as f

# This file is the starting point of the entire game.

while True:
    startup = input("Wanna play rock, paper, and scissors? (y/n)\nType \"cmds\" for special commands.\n")
    if startup.lower() == "y":
        f.play()
        break
    elif startup.lower() == "n" or startup.lower() == 'exit':
        print("Exiting...")
        sys.exit()
    elif startup.lower() == "cmds":
        commands.cmd()
        break
    else:
        print("Try again.")



# Version v1.0.0