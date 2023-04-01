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
            print("Wait Please to another sending SMS tool will automatically Re-load")
            time.sleep(8)
            return main()

        elif Choices_API == "2":
            Clear()
            tillow_api = config['Tillow']['account_sid']
            tillow_token = config['Tillow']['token_key']
            tillow_number = config['Tillow']['Tillow_number']
            print(f"APi info SMS Provider : \n")
            info_cred = TillowAccount(tillow_api,tillow_token,tillow_number).credential() 
            phone_numbers , message = Inputs()
            Provider = Tillow(tillow_api,
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
            info_cred = TextlocalAccount(txtlocal_api,txtlocal_sender).credential()
            phone_numbers , message = Inputs()
            Provider = Textlocal(txtlocal_api, 
                                 txtlocal_sender, 
                                 message, 
                                 phone_numbers)

            Provider.sms_sender()
            print("Wait Please to another sending SMS tool will automatically Re-load")
            time.sleep(8)
            return main()

        elif Choices_API == "4":
            Clear()
            textblte_api = config['textbelt']['api_key']
            print(f"API info SMS Provider : \n {textblte_api} ")
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

        APIs = ['Nexmo','Tillow','TextLocal','Textbelt']
        url  = "https://github.com/deep-matter/SMS-python-Sender"
        print(f"to be able to use this tool you should have one account at least \n")
        print(f"{[api for api in APIs ]} \n")
        print(f"Read documenatation in Repo {url} to see how to setup account Credentials") 
        time.sleep(8)
        return main()

    elif Choices == "3":
        
         Providers =  ['nexmo','tillow','textlocal','textbelt']
         url = "https://www.example.com"
         print(f" For more information of each API to create account see :\n")
         print(f" Nexmo Offcial website : {url}?ref={Providers[0]} \n")
         print(f" Tillow Offcial website : {url}?ref={Providers[1]} \n")
         print(f" Textlocal Offcial website : {url}?ref={Providers[2]} \n")
         print(f" Textbelt Offcial website : {url}?ref={Providers[3]} \n")
         time.sleep(8)
         return main()
    else:
        print("you insert invalide option the tool will reload automatically Please Wait ...")
        time.sleep(8)
        return main()


        



if __name__ == "__main__":
    main()  
