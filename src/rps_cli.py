from platform import python_version, system
from commands import *
from commands_help import *

commands = ['toggle_nonstop',
            'changedatacolor',
            'currentdatacolor',
            'game',
            'changecharttype',
            'currentcharttype',
            'isitnonstop',
            'resetsettings',
            'changeconsolecolor',
            'currentconsolecolor']
   
# Main cmd

def cmd():
    print("""
          List of available commands:
          - changedatacolor
          - toggle_nonstop
          - currentdatacolor
          - game
          - changecharttype
          - currentcharttype
          - isitnonstop
          - resetsettings
          - changeconsolecolor
          - currentconsolecolor

          Other commands:
          - python_version
          - system
          
          Type \"<command>\" to get started with the command.
          or type \"help <command>\" to see the usage and description of a command.""")
    while True:
        com = input(">> ")
        
        if com == "exit":
            break
        elif com == "rps":
            cmd()
        elif com == 'python_version':
            print(python_version())
        elif com == 'system':
            print(system())

# Calling commands

        if com == commands[0] or com == 'ns_tog':
            nonstop_toggle()    
        elif com == commands[1] or com == 'chdc':
            changedatacolor()
        elif com == commands[2] or com == 'cdc':
            currentdatacolor()
        elif com == commands[3] or com == 'g':
            game()
        elif com == commands[4] or com == 'chct': 
            changecharttype()
        elif com == commands[5] or com == 'cct':
            currentcharttype()
        elif com == commands[6] or com == 'isitns':
            isitnonstop()
        elif com == commands[7] or com == 'reset':
            resetsettings()
        elif com == commands[8] or com == 'chcc':
            changeconsolecolor()
        elif com == commands[9] or com == 'ccc':
            currentconsolecolor()
        
# Calling commands with usage argument
        
        
        if com == "help " + commands[0]:
            nonstop_toggle_help()
        elif com == "help " + commands[1]:
            changedatacolor_help()
        elif com == "help " + commands[2]:
            currentdatacolor_help()
        elif com == "help " + commands[3]:
            game_help()
        elif com == "help " + commands[4]:
            changecharttype_help()
        elif com == "help " + commands[5]:
            currentcharttype_help()
        elif com == "help " + commands[6]:
            isitnonstop_help()
        elif com == "help " + commands[7]:
            resetsettings_help()
        elif com == "help " + commands[8]:
            changeconsolecolor_help()
        elif com == "help " + commands[9]:
            currentconsolecolor_help()