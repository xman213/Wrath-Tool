from pystyle import *
import requests, random, threading, string, os
import os
import sys
import time
import random
import requests
import pystyle 
from pystyle import *
from time import sleep






def main():
    global proxysuse
    global proxyss
    global codeschecked
    ip_addresses = requests.get("https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt").text.splitlines()


    proxysuse = 0
    codeschecked = 0
    proxyss = [ ]
   
    def proxys():
        global codeschecked
        global proxysuse
        global proxyss
        threading.Timer(3.23416, proxys).start()
        proxyss = random.choice(ip_addresses)
        proxysuse += 1
       

    import random

    threads = 5000
    # ---

    def nitro():
        global proxyss
        global codeschecked
        global proxysuse
        while True:
        

        
        
         code = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
         r = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true',proxies={"socks5":proxyss})
         if r.status_code == 200:
            print(Colorate.Horizontal(Colors.red_to_green, f'Valid Code! | discord.gift/{code}'))  
            codeschecked += 1
            os.system(f'title Wrath Tool ¦ Proxys Used: '+ str(proxysuse)+' ¦ Codes Checked: '+str(codeschecked))
         else:
            print(Colorate.Horizontal(Colors.red_to_green, f'Invalid Code! | discord.gift/{code}'))
            codeschecked += 1
            os.system(f'title Wrath Tool ¦ Proxys Used: '+ str(proxysuse)+' ¦ Codes Checked: '+str(codeschecked))
            time.sleep(3)
        

    proxys()
            
    while True:
        if threading.active_count() < int(threads):
                threading.Thread(target=nitro).start()
