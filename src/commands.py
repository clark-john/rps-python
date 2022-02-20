from os import path, remove
from configparser import ConfigParser
from rps import play
from console_colors import consolecolor
from tkinter import messagebox as msgbox
import matplotlib.pyplot as mtp
import sys
from shutil import rmtree

config = ConfigParser()
config.read('./settings.ini')

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
    msgbox.showerror("Error", "Couldn\'t find settings.ini file.").

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
  if path.exists('./score.csv'):
    remove('score.csv')
    msgbox.showinfo('Success','Cleared the score successfully.')
  else:
    msgbox.showinfo('Clear score', 'score.csv not found.')
  