"""
in this script you will need to setup the APIs
account of each different Sender provider 

here list of APIs used 

www.txtlocal.com ==> api-account {
  
    username:"",
    password:"",
    Sender-Name:"",

}
www.twillo.com ==> api-account {



}

"""

class TextLocal:

    def __init__(self, api_key,username=None, password=None,Sender=None):

        self.Api_key = api_key
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
                'Api_key': self.Api_key,
                'Sender': self.Sender
                }
        for key , value in info_account.items():
            print(f"{key} is {value}")




        




