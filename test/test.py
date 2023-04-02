import urllib.request
import urllib.parse
import requests
import vonage

Client = vonage.Client(key="37063557",secret="eVxcCBmiJ50OZRnB")
Sms = vonage.Sms(Client)
Sender = "Youness"
respond_data = Sms.send_message({
            "from":Sender,
            "to":"212674105984",
            "text":"test youness"
})

if respond_data["messages"][0]["status"] == "0":
    print(" msg was sent ")
else:
    print(f"msg is not sent error : {respond_data['messages'][0]['error-text']}")

