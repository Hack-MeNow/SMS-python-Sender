import urllib.request as re
import urllib.parse as parse
from account_settings import TextLocal 
from tqdm import tqdm
from Config_APIs import ConfigApis

Keys_info = TextLocal(ConfigApis.txtlocal_api,"Youness","empyt","Do")

keys = {'api_key': Keys_info.api_key,
        'sender': Keys_info.Sender }
print(Keys_info.info_settings())

def Sender_Sms(list_number: list,message: str,Sender: str,api_key):
    data = parse.urlencode({
        'api_key': api_key,
        'list_number': list_number,
        'message': message,
        'sender': Sender
        })
    data = data.encode('utf-8')
    request = re.Request("https://api.textlocal.in/send/?")
    send_sms = re.urlopen(request, data)
    respond = send_sms.read()

    return respond

with open('list_number.txt','r') as file:
    phone_number = [line.strip() for line in file.readlines()]
   
for phone_number in tqdm(phone_number):
    message = "happy new year to us "
    send = Sender_Sms(phone_number, message, keys["sender"],keys["api_key"])
    tqdm.write(f"Logs of sending process \n sent to phone number {phone_number} \n Responding SMS {send} ")
