from os import path
from rps import play
from colorama import Fore, init, Style
from configparser import ConfigParser
from platform import python_version, system

init()
config = ConfigParser()
config.read('settings.ini')


commands = ['toggle_nonstop',
            'changedatacolor',
            'currentdatacolor',
            'game',
            'changecharttype',
            'currentcharttype',
            'isitnonstop',
            'resetsettings']

chart_types = ['bar',
               'dots',
               'plot',
               'stem',
               'step']

# Colorama Variables

r = Fore.RESET
bright = Style.BRIGHT
critical = Fore.RED + bright 
success = Fore.GREEN + bright
info = Fore.CYAN + bright
conf = Fore.YELLOW + bright

# Commands

def nonstop_toggle():
    if path.exists('./settings.ini'):
        print(conf + 'Turn on nonstop? (y/n)' + r)
        toggle = input().lower()
        if toggle == 'y':
            config.set('RPS', 'nonstop', 'True')
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success +'Nonstop set to True' + r)
        elif toggle == 'n':
            config.set('RPS', 'nonstop', 'False')
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Nonstop set to False' + r)
        elif toggle == 'exit':
            return
        else:
            print(critical +  + 'Invalid option.')
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)

def changedatacolor():
    if path.exists('./settings.ini'):
        datachartcolor = input("Type a name of color or hex code of a color.\n")
        if datachartcolor == "exit":
            return
        elif datachartcolor == '':
            print(critical + 'Data color cannot be null.' + r)
        else:
            config.set('Chart', 'datachartcolor', datachartcolor)
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Bar color updated successfully.' + r)
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)

def currentdatacolor():
    if path.exists('./settings.ini'):
        print(config.get('Chart', 'datachartcolor'))
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)

def game():
    play()


def currentcharttype():
    if path.exists('./settings.ini'):
        print(config.get('Chart', 'chart_type'))
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)

def changecharttype():
    if path.exists('./settings.ini'):
        charttype = input("Type a chart type (bar, plot, dots, step, stem)\n")
        if charttype == 'exit':
            return
        elif charttype not in chart_types:
            print(critical + f"A chart type \"{charttype}\" doesn't exist." + r)
        elif charttype == '':
            print(critical + 'Chart type cannot be null.' + r)
        else:
            config.set('Chart', 'chart_type', charttype)
            with open('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Chart type updated successfully.' + r)
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)
        
def isitnonstop():
    if path.exists('./settings.ini'):
        isitnonstop = config.get('RPS', 'nonstop')
        if isitnonstop == 'False':
            print("No")
        elif isitnonstop == 'True':
            print("Yes")
        else:
            print("Unknown")
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)

def resetsettings():
    if path.exists('./settings.ini'):
        print(conf + 'Are you sure? (y/n)' + r)
        confirm = input()
        if confirm == "y" or confirm == "Y":
            config.set('Chart', 'chart_type', 'bar')
            config.set('Chart', 'datachartcolor', 'dodgerblue')
            config.set('RPS', 'nonstop', 'False')
            with open('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Settings reset successfully.' + r)
        else:
            return
    else:
        print(critical + 'Couldn\'t find settings.ini file' + r)

# Commands with help

def nonstop_toggle_help():
    print("Usage: rps toggle_nonstop \n")
    print("Description: It prompts for turning the setting on or off. (i.e. nonstop is when the game will not prompt")
    print("you to play the game again, instead it repeats the game instantly, but you can stop the game by typing \"stop\"")
    
    
def changedatacolor_help():
    print("Usage: rps changedatacolor \n")
    print("Description: It prompts for changing the data color by hexcode or name of a color.")
    print("Make sure you add the \"#\" before the hexcode, or specify an appropriate name of a color.")
    

def currentdatacolor_help():
    print("Usage: rps currentdatacolor \n")
    print("Description: Returns the current data color.")

def game_help():
    print("Usage: rps game \n")
    print("Description: Plays the game.")
    
def changecharttype_help():
    print("Usage: rps changecharttype \n")
    print("Description: It prompts for changing the chart type.")
    
def currentcharttype_help():
    print("Usage: rps currentcharttype \n")
    print("Description: Returns the current chart type.")
    
# Main cmd

def cmd():
    print("""
          List of available commands: Prefix: rps
          - changedatacolor
          - toggle_nonstop
          - currentdatacolor
          - game
          - changecharttype
          - currentcharttype
          - isitnonstop
          - resetsettings
          
          Type \"rps <command>\" to get started with the command.
          or type \"rps usage <command>\" to see the usage and description of a command.""")
    while True:
        com = input(">> ")
        
        if com == "exit":
            break
        elif com == "rps":
            cmd()
        elif com == 'game':
            game()
        elif com == 'python_version':
            print(python_version())
        elif com == 'system':
            print(system())

# Calling commands

        if com == "rps " + commands[0]:
            nonstop_toggle()    
        elif com == "rps " + commands[1]:
            changedatacolor()
        elif com == "rps " + commands[2]:
            currentdatacolor()
        elif com == "rps " + commands[3]:
            game()
        elif com == "rps " + commands[4]:
            changecharttype()
        elif com == "rps " + commands[5]:
            currentcharttype()
        elif com == "rps " + commands[6]:
            isitnonstop()
        elif com == "rps " + commands[7]:
            resetsettings()
        
# Calling commands with usage argument
        
        
        if com == "rps usage " + commands[0]:
            nonstop_toggle_help()
        elif com == "rps usage " + commands[1]:
            changedatacolor_help()
        elif com == "rps usage " + commands[2]:
            currentdatacolor_help()
        elif com == "rps usage " + commands[3]:
            game_help()
        elif com == "rps usage " + commands[4]:
            changecharttype_help()
        elif com == "rps usage " + commands[5]:
            currentcharttype_help()