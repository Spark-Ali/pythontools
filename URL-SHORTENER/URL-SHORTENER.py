#Modules 
import pyshorteners #pip3 install pyshorteners(Restart Required)
import colorama
from colorama import Fore, Back, Style




#Styling
print(f'''{Fore.GREEN}
 _   _ ____  _         ____  _   _  ___  ____ _____ _____ _   _ _____ ____  
| | | |  _ \| |       / ___|| | | |/ _ \|  _ \_   _| ____| \ | | ____|  _ \ 
| | | | |_) | |   ____\___ \| |_| | | | | |_) || | |  _| |  \| |  _| | |_) |
| |_| |  _ <| |__|_____|__) |  _  | |_| |  _ < | | | |___| |\  | |___|  _ < 
 \___/|_| \_\_____|   |____/|_| |_|\___/|_| \_\|_| |_____|_| \_|_____|_| \_\\                                                                           

''')
link = input(f"{Fore.GREEN}Enter Your Link Which You Wanna Shortener : ")



#Logical
shorteners = pyshorteners.Shortener()
x = shorteners.tinyurl.short(link)
print('')
print(f"Your Link is Shortenered as {Fore.RED} {x}")

