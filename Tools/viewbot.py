


import random, threading, json, cursor, io, requests, os, sys, time
from pystyle import *
from bs4 import BeautifulSoup
from PIL import Image
from urllib.parse import unquote
from base64 import b64decode
import pystyle
from pystyle import *
def main():

    
    cursor.hide()
    import getpass
    vid = str(input(Colorate.Horizontal(Colors.red_to_green,f"enter you video id you would like to bot:")))
    class Viewbot:
        def __init__(self):
            self.logo()
            self.config = ['']

            #proxy = random.choice(open('./data/proxies.txt', 'r').read().splitlines())
            
            # self.proxies = {
            #     'http': f'http://{}',
            #     'https': f'http://{}'
            # }

            self.session = requests.Session()
            self.url     = "https://zefoy.com/"
            self.key, self.sessid = self.get_global_key()
            
            threading.Thread(target=self.title).start()
            

            self.send_views()
        
        def _print_(self, arg):
            sys.stdout.write(f"\r{arg}")
            sys.stdout.flush()
            
        def _print(self, fr):
            cursor.hide()
            os.system("cls" if os.name == "nt" else 'clear')
            txt = f'''{fr}
    '''

            print(Colorate.Horizontal(Colors.red_to_green, Center.XCenter(txt), 1))
        
        def logo(self):
            cursor.hide()
            txt = ''' '''
            
            print(Colorate.Horizontal(Colors.blue_to_green, Center.XCenter(txt), 1))
            
        def title(self):
            _t_ = time.time()
            while True:
                os.system(f"title LEAD TOOL ^| Elapsed: {round(time.time()- _t_, 1)} seconds ^| tk#1337 (.gg/onlp))")
                time.sleep(0.1)

        def get_global_key(self):

            """
            get sessid > get captcha > validate captcha > get global key
            :return:
            """

            sessid = self.session.get(
                self.url ,
                headers={
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                },
                #proxies = self.proxies
            ).cookies.values()[0]
            # This was a tool made to get perms in a server
            response = self.session.get(
                # All credits for this go to https://github.com/xtekky
                self.url  + "a1ef290e2636bf553f39817628b6ca49.php",
                headers={
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                    "cookie": f"PHPSESSID={sessid}",
                },
                params={
                    "_CAPTCHA": "",
                    "t": "0.23092200 1654778649"
                },
                #proxies = self.proxies
            )

            image = Image.open(io.BytesIO(response.content))
            image.show()

            _cap = Write.Input("Captcha > ", Colors.red_to_blue, interval=0.0001)
            image.close()
            print('\n')
            
            _response = self.session.post(
                self.url,
                data={
                    "captcha_secure": _cap,
                    "r75619cf53f5a5d7aa6af82edfec3bf0": ""
                },
                headers={
                    "cookie": f"PHPSESSID={sessid}",
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                },
                #proxies = self.proxies
            )

            soup = BeautifulSoup(_response.text, 'lxml')
            r = soup.find("div", {"id": "sid4"})
            key_1 = r.find("input", {"class": "form-control text-center font-weight-bold rounded-0"}).get("name")

            return key_1, sessid

        def send_views(self):
            while True:
                time.sleep(2)
                
                _request = self.session.post(
                    self.url + "c2VuZC9mb2xsb3dlcnNfdGlrdG9V",
                    headers={
                        "cookie": f"PHPSESSID={self.sessid}",
                        "origin": "https://zefoy.com",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest"
                    },
                    data={
                        self.key: f"https://www.tiktok.com/@{''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))}/video/"+vid
                    },
                    #proxies = self.proxies
                )
                obf_code = b64decode(unquote(_request.text[::-1])).decode("utf-8")

                if 'This service is currently not working' in obf_code:
                    self._print(' [ x ] Views not available in the moment')
                    input()
                    sys.exit()

                if 'Server too busy' in obf_code:
                    self._print(" [ x ] Server OverLoaded, Try again later!")
                    time.sleep(10)
                    continue

                if 'function updatetimer()' in obf_code:
                    #print(obf_code)
                    timer = int(obf_code.split("= ")[1].split("\n")[0])
                    self._print(f"Timer: {timer}s")
                    start_ = time.time()

                    while time.time() < start_ + timer:
                        self._print(f'Timer: {round((start_ + timer) - time.time(), 1)}s')
                        time.sleep(2)
                        
                    self._print("Sending views...")
                    continue

                soup = BeautifulSoup(obf_code, 'lxml')
                try:
                    key_v2 = soup.find("input", {"type": "text"}).get("name")
                except:
                    input(obf_code)
                    sys.exit()
                time.sleep(1)
                _st_ = time.time()
                _send_views = requests.post(
                    self.url + "c2VuZC9mb2xsb3dlcnNfdGlrdG9V",
                    headers={
                        "cookie": f"PHPSESSID={self.sessid}",
                        "origin": "https://zefoy.com",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest"
                    },
                    data={
                        key_v2: vid
                    },
                    #proxies = self.proxies
                )
                latency = round(time.time() - _st_, 2)
                if latency > 3:
                    self._print(" [ * ] sent views ! ")

                timer_obf = b64decode(unquote(_send_views.text[::-1])).decode("utf-8")
                if 'Too many requests. Please slow down.' in timer_obf:
                    self._print(" [ x ] Ratelimited")
                    time.sleep(120)
                    continue
                # print(timer_obf)
                timer = int(timer_obf.split("= ")[1].split("\n")[0])
                self._print(f" [ @ ] Cool Down: {timer}s")
                start_ = time.time()

                while time.time() < start_ + timer:
                    self._print(f' [ @ ] Cool Down: {round((start_ + timer) - time.time())}s')
                    time.sleep(2)
                
                self._print(" [ * ] Sending views...")

    Viewbot()
