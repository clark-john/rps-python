from colorama import Fore, init
from console_colors import consolecolor
init()
yel = Fore.YELLOW

# Commands with help

def nonstop_toggle_help():
  print("Description: It prompts for turning the setting on or off. (i.e. nonstop is when the game will not prompt")
  print("you to play the game again, instead it repeats the game instantly, but you can stop the game by typing \"stop\"")
  print("Alias: ns_tog")
    
def changedatacolor_help():
  print("Description: It prompts for changing the data color by hexcode or name of a color.")
  print("List of available named colors: "+yel+"https://matplotlib.org/stable/gallery/color/named_colors.html"+consolecolor)
  print("Alias: cdc")
    
def currentdatacolor_help():
  print("Description: Returns the current data color.")
  print("Alias: cdc")

def game_help():
  print("Description: Plays the game.")
  print("Alias: g")
    
def changecharttype_help():
  print("Description: It prompts for changing the chart type.")
  print("Alias: chct")
    
def currentcharttype_help():
  print("Description: Returns the current chart type.")
  print("Alias: cct")

def isitnonstop_help():
  print("Description: Returns \'Yes\' or \'No\' if the nonstop option is either enabled or disabled.")
  print("Alias: isitns")

def resetsettings_help():
  print("Description: Resets the entire settings.")
  print("Alias: reset")

def changeconsolecolor_help():
  print("Description: It prompts for changing the default console color.")
  print("Alias: chcc")

def currentconsolecolor_help():
  print("Description: Returns the current default console color.")    
  print("Alias: ccc")

def datacolorpreview_help():
  print("Description: Previews the current data color.")
  print("Alias: viewcolor")

def clearcache_help():
  print("Description: Clears the cache (__pycache).")
  print("Alias: uncache")

def clearscore_help():
  print("Description: Clears/resets the csv score file.")

def showcolorlist_help():
  print("Description: It shows the list of accepted color names.")
  print("Alias: colors")