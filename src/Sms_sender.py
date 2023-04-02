from .providers.Senders import * 
from .providers.account_settings import * 
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
    Screen_log()
    time.sleep(1)

def PrintC(message , Color):
    pass

def Inputs():
    phone_numbers = input("add the path list numbers: ")
    message = input("write the message SMS to send: ")
    return phone_numbers , message

def main():
     # Read file Credential APIs 
    config = ConfigParser()
    config.read("APIs_Accounts_Credentials.cfg") 
    Clear()
    print("1: Send SMS with different API providers")
    print("2: Help")
    print("3: more info about APIs send SMS-Providers Config")
    print("4: Exiting from tool Press CTRL + C ")
    Choices = input("\n Please insert the choice: ")
    
    # Send SMS with different API providers
    if Choices == "1":
        Clear()
        print("following API providers are available: \n 1. Nexmo APi \n 2. Twilio API  \n 3. Textlocal \n 4. Textbelt \n ")
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

            Provider = Nexmo(Nexmo_api,
                                   Nexmo_secret,
                                   Nexmo_Sender,
                                   message,
                                   phone_numbers)
            Provider.sms_sender()
            print("Wait Please to another sending SMS tool will automatically Re-load")
            time.sleep(8)
            return main()

        elif Choices_API == "2":
            Clear()
            tillow_api = config['Twillo']['account_sid']
            tillow_token = config['Twillo']['token_key']
            tillow_number = config['Twillo']['Twillo_number']
            print(f"APi info SMS Provider : \n")
            info_cred = TwilloAccount(tillow_api,tillow_token,tillow_number).credential()
            phone_numbers , message = Inputs()
            Provider = Twillo(tillow_api,
                                tillow_token,
                                tillow_number,
                                message,
                                phone_numbers)
            
            Provider.sms_sender()
            print("Wait Please to another sending SMS tool will automatically Re-load")
            time.sleep(8)
            return main()

        elif Choices_API == "3":
            Clear()
            txtlocal_api = config['Textlocal']['api_key']
            txtlocal_sender = config['Textlocal']['sender']
            print("API info SMS Provider: \n")
            info_cred = TextLocalAccount(txtlocal_api,txtlocal_sender).credential()
            phone_numbers , message = Inputs()
            Provider = TextLocal(txtlocal_api, 
                                 txtlocal_sender, 
                                 message, 
                                 phone_numbers)

            Provider.sms_sender()
            print("Wait Please to another sending SMS tool will automatically Re-load")
            time.sleep(20)
            return main()

#b'{"errors":[{"code":3,"message":"Invalid login details"}],"status":"failure"}'
        elif Choices_API == "4":
            Clear()
            textblte_api = config['textbelt']['api_key']
            print(f"API info SMS Provider \n Api key: {textblte_api} ")
            phone_numbers , message = Inputs()
            Provider = TextBelt(textblte_api , message , phone_numbers)
            Provider.sms_sender()
            print("Wait Please to another sending SMS tool will automatically Re-load")
            time.sleep(8)
            return main()
        else:
            print("you insert invalide option the tool will reload automatically Please Wait ...")
            time.sleep(8)
            return main()

    elif Choices == "2":
        Clear()
        APIs = ['Nexmo','Tillow','TextLocal','Textbelt']
        url  = "https://github.com/deep-matter/SMS-python-Sender"
        print(f"to be able to use this tool you should have one account at least \n")
        print(f"{[api for api in APIs ]} \n")
        print(f"Read documenatation in Repo {url} to see how to setup account Credentials") 
        time.sleep(8)
        return main()

    elif Choices == "3":
         Clear()
         Providers =  ['nexmo','tillow','textlocal','textbelt']
         print(f" For more information of each API to create account see :\n")
         print(f" Nexmo Offcial website : https://www.{Providers[0]}.com")
         print(f" Tillow Offcial website : https://www.{Providers[1]}.com")
         print(f" Textlocal Offcial website : https://www.{Providers[2]}.com")
         print(f" Textbelt Offcial website : https://www.{Providers[3]}.com")
         time.sleep(8)
         return main()
    else:
        print("you insert invalide option the tool will reload automatically Please Wait ...")
        time.sleep(8)
        return main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
    # Handle the KeyboardInterrupt exception (i.e. CTRL + C was pressed)
        print("\n Exiting tool...")
        sys.exit(0)   
