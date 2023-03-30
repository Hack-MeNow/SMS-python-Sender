"""
in this script you will need to setup the APIs
account of each different Sender provider 
here list of APIs used :
www.txtlocal.com ==> api-account {
    username:"",
    password:"",
    Sender-Name:"",
}
www.twillo.com ==> api-account {
}
"""
import json

class TextLocal:
    def __init__(self, api_key,username=None, password=None,Sender=None):
        self.api_key = api_key
        self.username = username
        self.password = password
        if Sender == "Dofus":
            self.Sender = "Dofus"
        else:
            self.Sender = Sender
    def info_settings(self):
        info_account = {
                'username': self.username,
                'password': self.password,
                'Api_key': self.api_key,
                'Sender': self.Sender
                }
        for key , value in info_account.items():
            print(f"{key} is {value}")

class Nexmo_config:
    def __init__(self, api_key, secret_key, Owner):
        
        self.api = api_key
        self.secret_key = secret_key
        self.Owner = Owner
    def credential(self):
        data_api = {
                "api_key": self.api,
                "secret_key":self.secret_key,
                "Owner-Sender":self.Owner
                }
        for key , value in data_api.items():
            print(f"{key} is :{value}")
     



        




