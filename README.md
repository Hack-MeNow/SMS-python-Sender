# SMS-python-Sender
![alt text](logo.png)

### how to use **TOOL**
this tool created to show how to Send SMS using Different APIs Providers under Lecience MIT
the rules of are :
* ***Educational Purpose***
* ***not responsible for Illigal use case***
* ***Share how to building Automated Tool*** 
### Installation 
* **install**</br>
the tool in Local machine , this version only support Linux Distro RUN Following command:

```sh
  chmod a+x installer.sh && ./installer.sh --install 
```
* **run**</br>
to run the tool make sure you already installed all the Packages :
  
```sh 
  ./installer.sh --run
```
* **help**</br>
check other availebel option RUN :

```sh 
  ./installer.sh --help 
```
### information about **Haydra-SMS** :
* **APIs Credentials :**
The tool created to Send SMS and Verification numbers , to be able to use the tool you have to have at least one of this account to access the APIs Credentials Visit the Offcial websites :

  * [**Nexmo**](https://www.nexmo.com)
  * [**Twillo**](https://www.twillo.com)
  * [**textlocal**](https://www.textlocal.com)
  * [**Textbelt**](https://www.Textbelt.com)

* **How to USE Tool:**
when you run the tool will show options , **SMS-python-Sender** provide many Providers APIs Senders , choice one you have **Credential API**

1. **OPTIONS**
    - **(1)** : is allowing to choice one APIs to send 
    - **FILE LIST NUMBERS** : you need to setup **list_number.txt** and set all the phone numbers you want to send SMS and **MAKE SURE TO WRITE NUMBER WITH COUNTRY CODE**

2. **EORRO HANDLING**
this tool is take considration of EORRR HANDLING which means it handle the respond Status if **SENT** or **ERROR**
