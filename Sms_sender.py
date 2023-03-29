from Senders import * 
from account_settings import * 
from configparser import ConfigParser 

# Read file Credential APIs 
config = ConfigParser()
config.read("APIs_Accounts_Credentials.cfg")
# get the APIs Credential
Nexmo_api = config['Nexmo_api']['api_key']
Nexmo_secret = config['Nexmo_api']['secret_key']
Nexmo_Sender = config['Nexmo_api']['sender']
print(Nexmo_api)
info_cred = Nexmo_config(Nexmo_api,Nexmo_secret,Nexmo_Sender).credential()

# Provider sending to chose
message = "hey haytam this is only the test APIs in morocco only now"
print(message)
list_number = 'list_number.txt'
Provider = NexmoSender(Nexmo_api,Nexmo_secret,Nexmo_Sender,message,list_number)
Provider.sms_sender() 



