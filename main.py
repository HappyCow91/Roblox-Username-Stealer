import requests
import time
from discord_webhook import DiscordWebhook
from colorama import *

## YOU SHOULD RUN THIS ON YOUR OWN CLOUD COMPUTER OR PYTHON CLOUD HOSTING SERVICE ##
# Not necessarily. It's fine to run it on your home computer
# but if you shut down your computer, the program will shut down too.

## FREE HOSTING >> https://pella.app

username = "PutUsername" # Roblox username you reported
webhook_url = "PutDiscordWebhook" # Discord webhook


# This program uses roproxy.com for anti-IP blocking
res = requests.get(f"https://auth.roproxy.com/v1/usernames/validate?Username={username}&Birthday=1337-01-01&Context=0")
while True:
    time.sleep(2.5)
    data = res.json()
    if data["code"] == 0:
        webhook = DiscordWebhook(url=webhook_url, content=f"@everyone Now ! You can using roblox username **{username}**\n\nhttps://www.roblox.com/CreateAccount << Make account")
        webhook.execute()
        print(f"[+] Username {username} successfully snipe !" + Fore.GREEN)
        break
    else:
        print(f"[-] {username} is already use (You should report it as an inappropriate name.) https://roblox.com/support" + Fore.RED)
