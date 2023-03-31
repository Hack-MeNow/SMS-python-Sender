from providers.Senders import * 
from providers.account_settings import * 
from configparser import ConfigParser 
from termcolor import colored
import sys  
import random
import time
import os

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

def Clear():
    os.system("clear")
    time.sleep(0.5)
    Screen_log()

def Inputs():
    phone_numbers = input("add the path list numbers: ")
    message = input("write the message SMS to send: ")
    return phone_numbers , message

def main():
     # Read file Credential APIs 
    config = ConfigParser()
    config.read("APIs_Accounts_Credentials.cfg")            
    Screen_log()
    print("1: Send SMS with different API providers")
    print("2: Help")
    print("3: more info about APIs send SMS-Providers Config")
    Choices = input("\n Please insert the chose: ")
    
    # Send SMS with different API providers
    if Choices == "1":
        print("following API providers are available: \n 1. Nexmo APi \n 2. Twilio API  \n 3. Textlocal \n ")
        Choices_API = input("which API provider you want to use: ")
        if Choices_API == "1":
            Clear()
           # get the APIs Credential
            Nexmo_api = config['Nexmo_api']['api_key']
            Nexmo_secret = config['Nexmo_api']['secret_key']
            Nexmo_Sender = config['Nexmo_api']['sender']
            print("info Provider API and secret key \n")
            info_cred = Nexmo_config(Nexmo_api,Nexmo_secret,Nexmo_Sender).credential()
            phone_numbers , message = Inputs()

            Provider = NexmoSender(Nexmo_api,
                                   Nexmo_secret,
                                   Nexmo_Sender,
                                   message,
                                   phone_numbers)
            Provider.sms_sender()
            return main()
            




if __name__ == "__main__":
    main()  
    






