from os import path, remove
from configparser import ConfigParser
from rps import play
from console_colors import consolecolor
from tkinter import messagebox as msgbox
import matplotlib.pyplot as mtp
from shutil import rmtree
from re import compile
from webbrowser import open_new_tab
from glob import glob
from time import sleep
import pyscreeze
from colorama import (
  init,
  Fore,
  Style
)

init()

# Colorama Variables:
yel = Style.BRIGHT + Fore.YELLOW 
gr = Style.BRIGHT + Fore.GREEN

config = ConfigParser()
config.read('./settings.ini')

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
  if path.exists('./settings.ini'):
    toggle = msgbox.askyesno("Enable Nonstop", "Turn on nonstop?")
    if toggle == True:
      config.set('RPS', 'nonstop', 'True')
      with open ('settings.ini', 'w') as settingsfile:
        config.write(settingsfile)
        msgbox.showinfo("Success", "Nonstop set to True")
    elif toggle == False:
      config.set('RPS', 'nonstop', 'False')
      with open ('settings.ini', 'w') as settingsfile:
        config.write(settingsfile)
        msgbox.showinfo("Success", "Nonstop set to False")
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def changedatacolor():
  color_list()
  if path.exists('./settings.ini'):

    datatype = input("Hex code or color name? (h/n)\n").lower()

    def set_color():
      config.set('Chart', 'datachartcolor', datachartcolor)
      with open ('settings.ini', 'w') as settingsfile:
        config.write(settingsfile)
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
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def currentdatacolor():
  if path.exists('./settings.ini'):
    print(config.get('Chart', 'datachartcolor'))
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def game():
  play()
  

def currentcharttype():
  if path.exists('./settings.ini'):
    print(config.get('Chart', 'chart_type'))
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def changecharttype():
  if path.exists('./settings.ini'):
    charttype = input("Type a chart type (bar, plot, dots, step, stem)\n")
    if charttype == 'exit':
      return
    elif charttype not in chart_types:
      msgbox.showerror('Error', f"A chart type \"{charttype}\" doesn't exist.")
    elif charttype == '':
      msgbox.showerror('Error', "Chart type cannot be null.")
    else:
      config.set('Chart', 'chart_type', charttype)
      with open('settings.ini', 'w') as settingsfile:
        config.write(settingsfile)
        msgbox.showinfo('Success', 'Chart type updated successfully.')
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")
      
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
      msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def resetsettings():
  if path.exists('./settings.ini'):
    confirm = msgbox.askyesno('Reset settings','Are you sure?')
    if confirm == True:
      config.set('Chart', 'chart_type', 'bar')
      config.set('Chart', 'datachartcolor', 'dodgerblue')
      config.set('RPS', 'nonstop', 'False')
      config.set('Console', 'default_console_color', 'cyan')
      with open('settings.ini', 'w') as settingsfile:
        config.write(settingsfile)
        msgbox.showinfo('Success', 'Settings reset successfully.')
    else:
      return
  else:
      msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def changeconsolecolor():
  if path.exists('./settings.ini'):   
    consolecol = input("Type a color of a console (red, green, blue, white, magenta, cyan, yellow)\n").lower()  
    if consolecol == 'exit':
      return
    elif consolecol not in console_colors:
      msgbox.showerror("Error", f"Console color \"{consolecol}\" doesn't exist.")
    elif consolecol == '':
      msgbox.showerror("Error", "Console color cannot be null.")
    else:
      config.set('Console', 'default_console_color', consolecol)
      with open('settings.ini', 'w') as settingsfile:
        config.write(settingsfile)
        msgbox.showinfo('Success', 'Console color updated successfully.')
        print("Type and enter \'restart\' to restart and apply changes.")
      
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def currentconsolecolor():
  if path.exists('./settings.ini'):
    print(config.get('Console', 'default_console_color'))
  else:
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.")

def datacolorpreview():
  x = ['A','B','C']
  y = [6,4,5]
  datacolor = config.get('Chart', 'datachartcolor')
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
  pyscreeze.screenshot('Screenshot.png')
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