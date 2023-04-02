import urllib.request as re
import urllib.parse as parse
import requests 
from tqdm import tqdm
import vonage
import json
from twilio.rest import Client
import os 
from colored import fg, bg, attr

RED = fg('red')
GREEN = fg('green')
WHITE = fg('white')

class TextLocal:
    def __init__(self,api_key ,sender, message,list_number: list):
        self.credential = {
            "api_key":api_key,
            "sender":sender
            }
        self.message = message
        self.list_number = self.read_file(list_number)

    @staticmethod 
    def read_file(file_list_number):
        with open(file_list_number,'r') as file:
            phone_number = [line.strip() for line in file.readlines()]
            return phone_number

    def config_Sms(self,api_key,phone_number,message,sender):
        data = parse.urlencode({
           'apikey': api_key,
           'numbers': phone_number,
           'message': message,
           'sender': sender
        })
        data = data.encode('utf-8')
        request = re.Request("https://api.textlocal.in/send/?")
        send_sms = re.urlopen(request, data)
        respond = send_sms.read()
        return respond

    def sms_sender(self):
        for phone_number in tqdm(self.list_number):
            message = "happy new year to us "
            send = self.config_Sms(self.credential["api_key"],phone_number,self.message,self.credential["sender"])
            send_= json.loads(send)
    
            if send_['status'] == "success":
                tqdm.write(f"{GREEN} sent : {WHITE } SMS to {phone_number} ")
            elif send_['errors'][0]['code'] == 3:
                tqdm.write(f"{RED} Error : {WHITE} SMS failure invalide credential or numbers")

class Nexmo:
    def __init__(self,api_key, secret_key,sender,message: str,list_number):
        self.credential = {
                "api_key":api_key,
                "secret_key":secret_key,
                "sender":sender
                }
        self.message =  message 
        self.phone_number = self.read_file(list_number)

    @staticmethod
    def read_file(list_number):
        with open(list_number,'r') as file:
            phone_number = [line.strip() for line in file.readlines()]
            return phone_number

    def sms_sender(self):
            for phone_number in tqdm(self.phone_number):
                sms_config = vonage.Client(key=self.credential["api_key"],secret=self.credential["secret_key"])
                check_credential = vonage.Sms(sms_config)

                Responding_sms = check_credential.send_message({
                        "from":self.credential["sender"],
                        "to": phone_number,
                        "text": self.message

                })
            ### check the status responding request
                if Responding_sms["messages"][0]["status"] == "0":
                    tqdm.write(f" {GREEN} Sent : {WHITE} SMS to phone_number:{phone_number}")
                else:
                    tqdm.write(f"{RED} failure to send Error is :{WHITE} {Responding_sms['messages'][0]['error-text']}")

class Twillo:
    def __init__(self,account_sid,auth_token,twillo_number,message,list_number):
        self.apikey = account_sid
        self.auth_token = auth_token 
        self.number_account = twillo_number
        self.message = message
        self.phone_number = self.read_file(list_number)

    @staticmethod
    def read_file(list_number):
        with open(list_number,'r') as file:
            phone_number = [line.strip() for line in file.readlines()]
            return phone_number

    def sms_sender(self):
        Client = Client(self.apikey,self.auth_token)
        for phone_number in tqdm(self.phone_number):
            try:
                SmsClient = Client.message.create(
                body = self.message,
                from_ = self.twillo_number,
                to = phone_number
                )
                if SmsClient.status == "sent":
                    tqdm.write(f"{GREEN} Sent :{WHITE} SMS to phone number : {phone_number} ")
            except ValueError():
                tqdm.write(f"{RED} Error :{WHITE} invalide number or check API auth ")
class TextBlet:
    def __init__(self,api_auth , message , list_number):

        self.api_auth = api_auth 
        self.message = message
        self.phone_number = self.read_file(list_number)

    @staticmethod
    def read_file(list_number):
        with open(list_number,'r') as file:
            phone_number = [line.strip() for line in file.readlines()]
            return phone_number

    def sms_sender(self):
        for phone_number in tqdm(self.phone_number):
            Responding_sms = requests.post('https://textbelt.com/text',{
            'phone': phone_number,
            'message':self.message,
            'key': self.api_auth
            })
            status = json.loads(Responding_sms)
            if status["status"] == 'true':
                tqdm.write(f"{GREEN} Sent: {WHITE} SMS to phone number : {phone_number}")
            else:
                tqdm.write("{RED} Error: {WHITE} invalide number")

