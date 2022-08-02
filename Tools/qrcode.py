import pyqrcode
import png
from pyqrcode import QRCode
import pystyle
from pystyle import *
def main():

    s = input(Colorate.Horizontal(Colors.red_to_green, "Enter URL: "))
    
    url = pyqrcode.create(s)
    url.png('WrathQRcode.png', scale = 6)