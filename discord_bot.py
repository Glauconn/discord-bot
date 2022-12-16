import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime, time
import asyncio

#set bot params and defines bot variable, ! as bot prefix, disables default help command, sets intents to default
intents = discord.Intents.default()
bot = Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents, help_command=None)


#reports to console when bot is primed and ready
@bot.event
async def on_ready() -> None:
  print(f"Logged in as {bot.user.name}")
  print("-----------------")

#function for a while True loop that posts 'working' to the general at 5:30pm daily
async def dailypost():
    await bot.wait_until_ready()
    while True:
        general = bot.get_channel("channel no. here")
        current_time = datetime.utcnow()
        if current_time.hour < 17 and current_time.minute == 30:
          await general.send('working')
        await asyncio.sleep(60)

#calls previous function as a loop
bot.loop.create_task(dailypost())

#Connects discord websocket and handles too many requests error
try:
    bot.run(os.getenv("TOKEN"))
except discord.HTTPException as e:
    if e.status == 429:
      print("The Discord servers denied the connection for making too many requests")
      print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
      print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
      os.system('kill 1')
    else:
        raise e