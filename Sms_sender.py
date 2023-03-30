from providers.Senders import * 
from providers.account_settings import * 
from configparser import ConfigParser 
from termcolor import colored
import sys  
import random
import time


def Screen_log():
    color_logo = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    random_color = random.choice(color_logo)
    print(colored(
    """

██╗░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░░░░░░░░██████╗███╗░░░███╗░██████╗
██║░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔════╝████╗░████║██╔════╝
███████║░╚████╔╝░██║░░██║██████╔╝███████║█████╗╚█████╗░██╔████╔██║╚█████╗░
██╔══██║░░╚██╔╝░░██║░░██║██╔══██╗██╔══██║╚════╝░╚═══██╗██║╚██╔╝██║░╚═══██╗
██║░░██║░░░██║░░░██████╔╝██║░░██║██║░░██║░░░░░░██████╔╝██║░╚═╝░██║██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═╝░░░░░╚═╝╚═════╝░

Created by Deep-Matter
Uploaded in term use educational Purpose 
use cases of this tool , the creator not responsbel for any illegal action
    """,
random_color))
    time.sleep(1)

def main():
    Screen_log()
    print("1: Send SMS with different API providers")
    print("2: Help")
    print("3: more info about APIs send SMS-Providers Config")
    Choices = print("\n Please insert the chose: ")
    
    

if __name__ == "__main__":
    main()  
    






