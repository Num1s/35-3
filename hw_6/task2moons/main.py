from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + 'green text')
print(Back.YELLOW + 'yellow back')
print(Style.BRIGHT + 'bright' + Style.RESET_ALL)
print('default')
