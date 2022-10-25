from colorama import Fore, init
from yamlparser import get_data

init()

yaml = get_data()

consolecolor = yaml['Console']['default_console_color']

match consolecolor:
	case 'cyan':
		consolecolor = Fore.CYAN
	case 'yellow':
		consolecolor = Fore.YELLOW
	case 'green':
		consolecolor = Fore.GREEN
	case 'magenta':
		consolecolor = Fore.MAGENTA
	case 'red':
		consolecolor = Fore.RED
	case 'white':
		consolecolor = Fore.WHITE
	case '_':
		pass
