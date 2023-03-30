import urllib.request as re
import urllib.parse as parse
import requests 
from tqdm import tqdm
import vonage

class TextLocalSender:
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
    def config_Sms(self,api_key,phone_number,message,sender):
        data = parse.urlencode({
           'apikey': api_key,
           'list_number': phone_number,
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
            tqdm.write(f"Logs of sending process \n sent to phone number {phone_number} \n Responding SMS {send} ")

class NexmoSender:
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
                    tqdm.write(f"the sms was sent succssfully to phone_number:{phone_number}")
                else:
                    tqdm.write(f"Sms failde to send Error is :{Responding_sms['messages'][0]['error-text']}")

