#IMPORTS
import requests
import colorama
from colorama import Fore, Back, Style


#Styling
print(f'''{Fore.GREEN}
__        _______ ____         ____ ___  _   _ _   _ _____ ____ _____ ___ 
\ \      / / ____| __ )       / ___/ _ \| \ | | \ | | ____/ ___|_   _|_ _|
 \ \ /\ / /|  _| |  _ \ _____| |  | | | |  \| |  \| |  _|| |     | |  | | 
  \ V  V / | |___| |_) |_____| |__| |_| | |\  | |\  | |__| |___  | |  | | 
   \_/\_/  |_____|____/       \____\___/|_| \_|_| \_|_____\____| |_| |___|
                                                                          
__     _____ _______   __     ____ _   _ _____ ____ _  _______ ____  
\ \   / /_ _|_   _\ \ / /    / ___| | | | ____/ ___| |/ / ____|  _ \ 
 \ \ / / | |  | |  \ V /____| |   | |_| |  _|| |   | ' /|  _| | |_) |
  \ V /  | |  | |   | |_____| |___|  _  | |__| |___| . \| |___|  _ < 
   \_/  |___| |_|   |_|      \____|_| |_|_____\____|_|\_\_____|_| \_\\
                                                                     

                                                         

''')
url = input("Enter The URL of SITE You Wanna Check for Connectivity : ")

timeout = 5
while True:
    try:
        request = requests.get(url, timeout=timeout)
        print('Connected')
    except KeyboardInterrupt:
        print("KeyBoard Interrupted Exiting!")
        exit()
    except:
        print(f"{Fore.RED}Not Connected")
        exit()
    
