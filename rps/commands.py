import sys
import os
import configparser
import rps

config = configparser.ConfigParser()
config.read('settings.ini')


commands = ['toggle_nonstop',
            'changedatacolor',
            'currentdatacolor',
            'game',
            'changecharttype',
            'currentcharttype']

chart_types = ['bar',
               'dots',
               'plot',
               'stem',
               'step']


# Commands

def nonstop_toggle():
    if os.path.exists('./settings.ini'):
        toggle = input("Turn on nonstop? (y/n)\n")
        if toggle.lower() == 'y':
            config.set('RPS', 'nonstop', 'True')
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print('Nonstop set to True')
        elif toggle.lower() == 'n':
            config.set('RPS', 'nonstop', 'False')
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print('Nonstop set to False')
        elif toggle.lower() == 'exit':
            return
        else:
            print('Invalid option.')
    else:
        print('Cannot find settings.ini file')

def changedatacolor():
    if os.path.exists('./settings.ini'):
        datachartcolor = input("Type a name of color or hex code of a color.\n")
        if datachartcolor == "exit":
            return
        elif datachartcolor == '':
            print('Data color cannot be null.')
        else:
            config.set('Chart', 'datachartcolor', datachartcolor)
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print('Bar color updated successfully.')
    else:
        print('Cannot find settings.ini file')

def currentdatacolor():
    if os.path.exists('./settings.ini'):
        print(config.get('Chart', 'datachartcolor'))
    else:
        print('Cannot find settings.ini file')

def game():
    rps.play()


def currentcharttype():
    if os.path.exists('./settings.ini'):
        print(config.get('Chart', 'chart_type'))
    else:
        print('Cannot find settings.ini file')

def changecharttype():
    if os.path.exists('./settings.ini'):
        charttype = input("Type a chart type (bar, plot, dots, step, stem)\n")
        if charttype == 'exit':
            return
        elif charttype not in chart_types:
            print(f"A chart type \"{charttype}\" doesn't exist.")
        elif charttype == '':
            print('Chart type cannot be null.')
        else:
            config.set('Chart', 'chart_type', charttype)
            with open('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print('Chart type updated successfully.')
        
    else:
        print('Cannot find settings.ini file')

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