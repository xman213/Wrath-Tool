import pyfiglet
import sys
import socket
from datetime import datetime
import pystyle
from pystyle import *


def main():
    target = input(Colorate.Horizontal(Colors.red_to_green, "Enter ip: "))

    if len(sys.argv) == 2:
        
        
        target = socket.gethostbyname(sys.argv[1])
    else:
        print(Colorate.Horizontal(Colors.red_to_green,"Invalid amount of Argument"))
    

    print(Colorate.Horizontal(Colors.red_to_green,"-" * 50))
    print(Colorate.Horizontal(Colors.red_to_green,"Scanning Target: " + target))
    print(Colorate.Horizontal(Colors.red_to_green,"Scanning started at:" + str(datetime.now())))
    print(Colorate.Horizontal(Colors.red_to_green,"-" * 50))
    
    try:
        
    
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            
            result = s.connect_ex((target,port))
            if result ==0:
                print(Colorate.Horizontal(Colors.red_to_green,"Port {} is open".format(port)))
            s.close()
            
    except KeyboardInterrupt:
            print(Colorate.Horizontal(Colors.red_to_green,"\n Exiting Program !!!!"))
            sys.exit()
    except socket.gaierror:
            print(Colorate.Horizontal(Colors.red_to_green,"\n Hostname Could Not Be Resolved !!!!"))
            sys.exit()
    except socket.error:
            print(Colorate.Horizontal(Colors.red_to_green,"\ Server not responding !!!!"))
            sys.exit()