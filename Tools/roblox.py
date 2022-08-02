import pystyle
from pystyle import *
import random
from random import randint
import time
def main():
    gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    total = input(Colorate.Horizontal(Colors.red_to_green,"How Many Would You Like To Generate? "))
    #Number To Generate
    number = int(total)



    for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            space1 = "-"
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            space2 = "-"
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)


            print(Colorate.Horizontal(Colors.red_to_green,generate1+generate2+generate3+space1+generate4+generate5+space1+generate6+space2+generate7+generate8+generate9+space2+generate10))

