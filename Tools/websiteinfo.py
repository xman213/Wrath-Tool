import dns
import dns.resolver
import pystyle
from pystyle import *
def main():
    url = input(Colorate.Horizontal(Colors.red_to_green,"Enter domain: "))
    result = dns.resolver.resolve(url, 'MX')
    for exdata in result:
        print (Colorate.Horizontal(Colors.red_to_green,' MX Record: '+str(exdata.exchange)))