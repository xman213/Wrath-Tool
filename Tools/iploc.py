import requests
import pystyle 
from pystyle import *
import geocoder

def main():
    ip  = input(Colorate.Horizontal(Colors.red_to_green, "Enter ip: "))

    import requests

    key = '8afd579c95c744178f55abd5ea6ed29d'



    r = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + key + '&ip_address=' + ip)
    data = r.json()
    city = data['city']
    state = data['region']
    contry = data['country']
    zipcode = data['postal_code']
    print(Colorate.Horizontal(Colors.red_to_green, f"Location info for: {ip}"))
    print(Colorate.Horizontal(Colors.red_to_green,"City: "+ city))
    print(Colorate.Horizontal(Colors.red_to_green, "State: " +state))
    print(Colorate.Horizontal(Colors.red_to_green, "Country: " +contry))
    print(Colorate.Horizontal(Colors.red_to_green, "Zip/Poastal Code: "+zipcode))
