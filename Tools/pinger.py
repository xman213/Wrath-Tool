import os
import subprocess
import pystyle
from pystyle import *
import threading

def main():
    global ip
    ip = input(Colorate.Horizontal(Colors.red_to_green, "Enter the ip/url you want to ping: " ))
    

    def ping():
     while True:
        response = os.popen(f"ping {ip}").read()
        if "Received = 4" in response:
            print(Colorate.Horizontal(Colors.red_to_green,f"{ip} Is online"))
        else:
            print(Colorate.Horizontal(Colors.red_to_green,f"{ip} is down"))
    threads = 500
          
    while True:
        if threading.active_count() < int(threads):
                threading.Thread(target=ping).start()


   


