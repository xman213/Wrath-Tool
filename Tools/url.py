import socket
import pystyle
from pystyle import *
def main():
    url = input(Colorate.Horizontal(Colors.red_to_green,"Enter domain name: "))
    print(Colorate.Horizontal(Colors.red_to_green,socket.gethostbyname(url)))
