import re, requests

from colorama import Fore, init
from discord.ext import commands
import pystyle
from pystyle import *
def main():
    init()
    RithSniper = commands.Bot(command_prefix="!", help_command=None, self_bot=False)

    nitro_redeem_token = input(Colorate.Horizontal(Colors.red_to_green,"Enter your token: "))


    @RithSniper.event
    async def on_connect():
        print('We have logged in as {0.user}'.format(RithSniper))


    @RithSniper.event
    async def on_message(message):
        try:
            if 'discord.gift/' in message.content:
                code = re.search("discord.gift/(.*)", message.content).group(1)
                headers = {
                    'Authorization': nitro_redeem_token,
                    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                "discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36 "
                }
                nitro = f"{Fore.MAGENTA}{Fore.RESET} Code: {Fore.BLUE}{code} {Fore.RESET}| "
                r = requests.post(
                    f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                    headers=headers)
                if '{"message": "Unknown Gift Code", "code": 10038}' in r.text:
                    print(nitro + Fore.RED + "INVALID CODE!")
                elif '{"message": "This gift has been redeemed already.", "code": 50050}' in r.text:
                    print(nitro + Fore.YELLOW + "ALREADY REDEEMED!")
                elif 'You are being rate limited' in r.text:
                    print(nitro + Fore.RED + "RATE LIMITED!")
                elif 'Access denied' in r.text:
                    print(nitro + Fore.RED + "DENIED ACCESS!")
                elif 'subscription_plan' in r.text:
                    print(nitro + Fore.GREEN + "REDEEMED!!")
        except AttributeError:
            pass


    RithSniper.run(nitro_redeem_token, bot=False)