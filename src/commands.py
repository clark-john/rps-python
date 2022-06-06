import matplotlib.pyplot as mtp
from os import path, remove
from yamlparser import get_data, set_data
from rps import play
from console_colors import consolecolor
from tkinter import messagebox as msgbox
from shutil import rmtree
from re import compile
from webbrowser import open_new_tab
from glob import glob
from time import sleep
from pyscreenshot import grab
from colorama import (
  init,
  Fore,
  Style
)

init()

# Colorama Variables:
yel = Style.BRIGHT + Fore.YELLOW 
gr = Style.BRIGHT + Fore.GREEN

yaml = get_data()

hex_pattern = compile('^[a-fA-F\\d]{6}$')

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

def color_list():
  global colors
  with open('colors.txt', 'r') as f:
    d = f.readlines()
    colors = []
    for x in d:
      e = x.strip().lower()
      colors.append(e)

# Commands

def nonstop_toggle():
  if path.exists('./settings.yml'):
    toggle = msgbox.askyesno("Enable Nonstop", "Turn on nonstop?")
    if toggle == True:
      yaml['RPS']['nonstop'] = True
      set_data(yaml)
      msgbox.showinfo("Success", "Nonstop set to True")
    elif toggle == False:
      yaml['RPS']['nonstop'] = False
      set_data(yaml)
      msgbox.showinfo("Success", "Nonstop set to False")
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def changedatacolor():
  color_list()
  if path.exists('./settings.yml'):

    datatype = input("Hex code or color name? (h/n)\n").lower()

    def set_color():
      yaml['Chart']['datachartcolor'] = datachartcolor
      set_data(yaml)
      msgbox.showinfo('Success', 'Bar color updated successfully.')

    if datatype == 'h':
      datachartcolor = input("Type a hexadecimal code for a color.\n")
      if datachartcolor == "exit":
        return
      elif datachartcolor == '':
        msgbox.showerror('Error', "Bar color cannot be null.")
      elif hex_pattern.match(datachartcolor) == None:
        msgbox.showerror('Error', "Invalid hex code.")
      else:
        datachartcolor = f"#{datachartcolor}"
        set_color()
    elif datatype == 'n':
      datachartcolor = input("Type a name of a color.\n")
      if datachartcolor not in colors:
        msgbox.showerror('Error', "Invalid color name.")
      elif datachartcolor == '':
        msgbox.showerror('Error', "Bar color cannot be null.") 
      elif datachartcolor == 'exit':
        return
      else:
        set_color()

    elif datatype == 'exit':
      return

  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def currentdatacolor():
  if path.exists('./settings.yml'):
    print(yaml['Chart']['datachartcolor'])
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def game():
  play()
  

def currentcharttype():
  if path.exists('./settings.yml'):
    print(yaml['Chart']['chart_type'])
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def changecharttype():
  if path.exists('./settings.yml'):
    charttype = input("Type a chart type (bar, plot, dots, step, stem)\n")
    if charttype == 'exit':
      return
      # panahong walang alam kung pano gamitin ang return na keyword :) jan-feb
    elif charttype not in chart_types:
      msgbox.showerror('Error', f"A chart type \"{charttype}\" doesn't exist.")
    elif charttype == '':
      msgbox.showerror('Error', "Chart type cannot be null.")
    else:
      yaml['Chart']['chart_type'] = charttype
      set_data(yaml)  
      msgbox.showinfo('Success', 'Chart type updated successfully.')
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")
      
def isitnonstop():
  if path.exists('./settings.yml'):
    isitnonstop = yaml['RPS']['nonstop']
    if isitnonstop == False:
      print("No")
    elif isitnonstop == True:
      print("Yes")
    else:
      print("Unknown")
  else:
      msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def resetsettings():
  if path.exists('./settings.yml'):
    confirm = msgbox.askyesno('Reset settings','Are you sure?')
    if confirm == True:
      yaml['Chart']['chart_type'] = 'bar'
      yaml['Chart']['datachartcolor'] = 'dodgerblue'
      yaml['RPS']['nonstop'] = False
      yaml['Console']['default_console_color'] = 'cyan'
      set_data(yaml)
      msgbox.showinfo('Success', 'Settings reset successfully.')
    else:
      return
  else:
      msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def changeconsolecolor():
  if path.exists('./settings.yml'):   
    consolecol = input("Type a color of a console (red, green, blue, white, magenta, cyan, yellow)\n").lower()  
    if consolecol == 'exit':
      return
    elif consolecol not in console_colors:
      msgbox.showerror("Error", f"Console color \"{consolecol}\" doesn't exist.")
    elif consolecol == '':
      msgbox.showerror("Error", "Console color cannot be null.")
    else:
      yaml['Console']['default_console_color'] = consolecol
      set_data(yaml)
      msgbox.showinfo('Success', 'Console color updated successfully.')
      print("Restart this program to apply changes.")
      
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def currentconsolecolor():
  if path.exists('./settings.yml'):
    print(yaml['Console']['default_console_color'])
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.yml file.")

def datacolorpreview():
  x = ['A','B','C']
  y = [6,4,5]
  datacolor = yaml['Chart']['datachartcolor']
  mtp.bar(x, y, color=datacolor)
  mtp.title('Data Color Preview')
  mtp.show()

def clearcache():
  if path.exists('./__pycache__'):
    rmtree('__pycache__')
    msgbox.showinfo('Success','Cleared the cache successfully.')
  else:
    msgbox.showinfo('Clear cache', '__pycache__ folder not found.')

def clearscore():
  if path.exists('./score.csv') or path.exists('./score.png'):
    gl = glob('score*')
    for file in gl:
      remove(file)
    msgbox.showinfo('Success','Cleared the score successfully.')
  else:
    msgbox.showinfo('Clear score', 'Already cleared the scores.')

def showcolorlist():
  with open('colors.txt', 'r') as colors:
    print(colors.read())

def screenshot():
  ss = 3
  while ss >= 0:
    print(f"Screenshotting in {ss}")
    sleep(1)
    ss -= 1
  image = grab()
  image.save('Screenshot.png')
  print("Screenshot done")

def repolink():
  print(gr+"https://github.com/clark-john/rps-python"+yel)
  print("View on browser? (y/n)"+consolecolor)
  op = input().lower()
  if op == 'y':
    open_new_tab('https://github.com/clark-john/rps-python')
  else:
    return

def creator():
  print(gr+"clark-john a.k.a. Clark"+yel)
  print("View on browser? (y/n)"+consolecolor)
  op = input().lower()
  if op == 'y':
    open_new_tab('https://github.com/clark-john')
  else:
    return