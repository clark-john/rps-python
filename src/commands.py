from os import path
from configparser import ConfigParser
from colorama import Fore, init, Style
from rps import play
from console_colors import consolecolor

init()

config = ConfigParser()
config.read('./settings.ini')

# Colorama Variables

r = consolecolor
bright = Style.BRIGHT
critical = Fore.RED + bright 
success = Fore.GREEN + bright
info = Fore.CYAN + bright
conf = Fore.YELLOW + bright

chart_types = ['bar',
               'dots',
               'plot',
               'stem',
               'step']

console_colors = [
                'red',
                'green',
                'blue',
                'cyan',
                'magenta',
                'white',
                'yellow'
                    ]

# Commands

def nonstop_toggle():
    if path.exists('./settings.ini'):
        print(conf + 'Turn on nonstop? (y/n)'+r)
        toggle = input().lower()
        if toggle == 'y':
            config.set('RPS', 'nonstop', 'True')
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success +'Nonstop set to True'+r)
        elif toggle == 'n':
            config.set('RPS', 'nonstop', 'False')
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Nonstop set to False'+r)
        elif toggle == 'exit':
            return
        else:
            print(critical +  + 'Invalid option.'+r)
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)

def changedatacolor():
    if path.exists('./settings.ini'):
        datachartcolor = input("Type a name of color or hex code of a color.\n")
        if datachartcolor == "exit":
            return
        elif datachartcolor == '':
            print(critical + 'Data color cannot be null.'+r)
        else:
            config.set('Chart', 'datachartcolor', datachartcolor)
            with open ('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Bar color updated successfully.'+r)
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)

def currentdatacolor():
    if path.exists('./settings.ini'):
        print(config.get('Chart', 'datachartcolor'))
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)

def game():
    play()


def currentcharttype():
    if path.exists('./settings.ini'):
        print(config.get('Chart', 'chart_type'))
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)

def changecharttype():
    if path.exists('./settings.ini'):
        charttype = input("Type a chart type (bar, plot, dots, step, stem)\n")
        if charttype == 'exit':
            return
        elif charttype not in chart_types:
            print(critical + f"A chart type \"{charttype}\" doesn't exist."+r)
        elif charttype == '':
            print(critical + 'Chart type cannot be null.'+r)
        else:
            config.set('Chart', 'chart_type', charttype)
            with open('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Chart type updated successfully.'+r)
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)
        
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
        print(critical + 'Couldn\'t find settings.ini file'+r)

def resetsettings():
    if path.exists('./settings.ini'):
        print(conf + 'Are you sure? (y/n)'+r)
        confirm = input()
        if confirm == "y" or confirm == "Y":
            config.set('Chart', 'chart_type', 'bar')
            config.set('Chart', 'datachartcolor', 'dodgerblue')
            config.set('RPS', 'nonstop', 'False')
            config.set('Console', 'default_console_color', 'cyan')
            with open('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Settings reset successfully.'+r)
        else:
            return
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)

def changeconsolecolor():
    if path.exists('./settings.ini'):   
        consolecol = input("Type a color of a console (red, green, blue, white, magenta, cyan, yellow)\n").lower()  
        if consolecol == 'exit':
            return
        elif consolecol not in console_colors:
            print(critical + f"Console color \"{consolecol}\" doesn't exist."+r)
        elif consolecol == '':
            print(critical + 'Console color cannot be null.'+r)
        else:
            config.set('Console', 'default_console_color', consolecol)
            with open('settings.ini', 'w') as settingsfile:
                config.write(settingsfile)
                print(success + 'Console color updated successfully.'+r)
                print("Restart to apply the changes.")
        
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)

def currentconsolecolor():
    if path.exists('./settings.ini'):
        print(config.get('Console', 'default_console_color'))
    else:
        print(critical + 'Couldn\'t find settings.ini file'+r)