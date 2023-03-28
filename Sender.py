import urllib.request as re
import urllib.parse as parse
from account_settings import TextLocal 
from tqdm import tqdm
#Keys = TextLocal("lkdbhbsjbdj:s@kknsjdb/khfkn><?","Youness","empyt","Dofus")

keys = {'api_key': TexitLocal.api_key,
        'sender': TextLocal.Sender }


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

    return (respond)

with open('list_number.txt','r') as file:
    phone_number = [line.strip() for line in file.readlines()]
   
for phone_number in tqdm(phone_number):
    message = "happy new year to us "
    send = Sender_Sms(phone_number, message, key.sender,key.api_key)
    tqdm.write(f"Logs of sending process \n sent to phone number {phone_numver} \n Responding SMS {send} ")
