import random
import time
import os
from tqdm import tqdm
import shutil
import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
import pandas as pd 
import requests

def read_file(file_list_number):
    with open(file_list_number,'r') as file:
        phone_number = ['+' + line.strip() for line in file.readlines()]
    return phone_number

def phone_validation(phone_list):
    phone_number = read_file(phone_list)
    DataNumbers = {
            'valid_number':[],
            'possible_number':[],
            'Carrier':[],
            'timezone':[],
            'Region':[]
            } 
    for phoneNumber in tqdm(phone_number):
        phone = phonenumbers.parse(phoneNumber)
        timeZone = timezone.time_zones_for_number(phone)[0]
        Carrier = carrier.name_for_number(phone,'en')
        Region = geocoder.description_for_number(phone,'en')
        DataNumbers['Carrier'].append(Carrier)
        DataNumbers['Region'].append(Region)
        DataNumbers['timezone'].append(timeZone)
        valid_number = phonenumbers.is_valid_number(phone)
        possible_number = phonenumbers.is_possible_number(phone)
        DataNumbers['valid_number'].append(valid_number)
        DataNumbers['possible_number'].append(possible_number)
    DataNumbers['phone_number']= phone_number
    # convert to dataframe and filtter only Valide number
    df = pd.DataFrame(DataNumbers).set_index('phone_number')
    df_= df[df['valid_number'] == True]
    # Save the File Execl with all the Columns
    if os.path.exists('output'):
        shutil.rmtree('output')

    if not os.path.exists('output'):
        os.makedirs('output',exist_ok=True)
        df_.to_csv('output/valide_number.csv',sep='\t',index=False)
        df.to_csv('output/DataNumbers.csv',sep='\t',index=False)
        # Save the File into Texr only valide number
        with open('output/valide_number.txt','w') as file:
            file.write('\n'.join(df_.index.tolist()))

    return df_ , df
def API_Number(phone_list):
    api_key = '33hIeqfPQ38znh6YrLq3udN59efWKSdP'
    phone_number = read_file(phone_list)
    for phoneNumber in tqdm(phone_number):
        url = f'https://apilayer.net/api/validate?access_key={api_key}&number={phoneNumber}'

        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            print(result)
            if result['valid']:

                print(f'{phone_number} is a valid phone number')
            else:
                 print(f'{phone_number} is not a valid phone number')
        else:
            print('Failed to validate phone number')
