import discord, threading, os
from pystyle import *


 

def main():
  client = discord.Client()
  os.system("mode con:cols=60 lines=26")

  dms = 0
  dmsf = 0

  token = input(Colorate.Horizontal(Colors.red_to_green,"> User Token: "))
  threads = input(Colorate.Horizontal(Colors.red_to_green, '> Threads: '))
  friends = (int(input(Colorate.Horizontal(Colors.red_to_green, '> How many friends does the token have: '))))
 
  while True:
     message = input(Colorate.Horizontal(Colors.red_to_green,"> Message to send: "))
     if message=="text":
         exit(0)
     else:
         print(Colorate.Horizontal(Colors.red_to_green, f"> Sending | {message}"))
         break
 
  @client.event
  async def on_connect():
   global dms
   global dmsf
   global friends
   for user in client.user.friends:
     try:
       await user.send(message)
       print(Colorate.Horizontal(Colors.red_to_green,f"> Sent | {message} | to: {user.name}"))
       dms += 1
       friends -=1
     except:
        print(Colorate.Horizontal(Colors.red_to_green,f"> Error Sending | {message} | to: {user.name}"))
        dmsf += 1
        friends -=1
        
  if threading.active_count() < int(threads):
           threading.Thread(target=on_connect).start()
 
  client.run(token, bot=False)
