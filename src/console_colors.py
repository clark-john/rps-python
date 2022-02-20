from configparser import ConfigParser
from colorama import Fore, init

init()
config = ConfigParser()
config.read('./settings.ini')

consolecolor = config.get('Console', 'default_console_color')

if consolecolor == 'cyan':
	consolecolor = Fore.CYAN
elif consolecolor == 'yellow':
	consolecolor = Fore.YELLOW
elif consolecolor == 'green':
	consolecolor = Fore.GREEN
elif consolecolor == 'magenta':
	consolecolor = Fore.MAGENTA
elif consolecolor == 'red':
	consolecolor = Fore.RED
elif consolecolor == 'white':
	consolecolor = Fore.WHITE
elif consolecolor == 'yellow':
	consolecolor = Fore.YELLOW