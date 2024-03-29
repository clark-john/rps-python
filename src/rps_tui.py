from platform import python_version, system
from commands import *
from commands_help import *

commands = [
	'toggle_nonstop', #0
	'changedatacolor', #1
	'currentdatacolor', #2
	'game', #3
	'changecharttype', #4
	'currentcharttype', #5
	'isitnonstop', #6
	'resetsettings', #7
	'changeconsolecolor', #8
	'currentconsolecolor', #9
	'datacolorpreview', #10
	'clearcache', #11
	'clearscore', #12
	'showcolorlist', #13
	'screenshot', #14
	'repolink', #15
	'creator', #16
]
   
# Main cmd

def cmd():

	rps_tui = """
	Welcome to rps-tui!

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
	  - datacolorpreview
	  - clearcache
	  - clearscore
	  - showcolorlist

	  Special:
	  - screenshot
	  - creator
	  - repolink

	  Other commands:
	  - python_version
	  - system
	  - rps
	  
	  Type any of these commands to execute.
	  Type \"help <command>\" to see the usage and description of a command.
	  Type \"help others\" for help of other commands.
"""

	print(rps_tui)
	while True:
		com = input(">> ")
		
		if com == "exit":
			break
		elif com == "rps":
			print(rps_tui)
		elif com == 'python_version':
			print(python_version())
		elif com == 'system':
			print(system())
		elif com == 'help others':
			print("python_version: Returns your current Python version.")
			print("system: Returns system you're using.")
			print("rps: Returns commands list.")

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
		elif com == commands[10] or com == 'viewcolor':
			datacolorpreview()
		elif com == commands[11] or com == 'uncache':
			clearcache()
		elif com == commands[12] or com == 'unsc':
			clearscore()
		elif com == commands[13] or com == 'colors':
			showcolorlist()
		elif com == commands[14] or com == 'ss':
			screenshot()
		elif com == commands[15] or com == 'repo':
			repolink()
		elif com == commands[16]:
			creator()

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
		elif com == "help " + commands[10]:
			datacolorpreview_help()
		elif com == "help " + commands[11]:
			clearcache_help()
		elif com == "help " + commands[12]:
			clearscore_help()
		elif com == "help " + commands[13]:
			showcolorlist_help()
		elif com == "help " + commands[14]:
			screenshot_help()
		elif com == "help " + commands[15]:
			repolink_help()
		elif com == "help " + commands[16]:
			creator_help()
