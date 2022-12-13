import discord
import os
from discord.ext import commands#, tasks
from discord.ext.commands import Bot
from datetime import datetime, time#, timedelta
import asyncio

##prefix to be entered before commands i.e. !test
intents = discord.Intents.default()
bot = Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents, help_command=None) ##sets ! prefix and removes default help command
WHEN = time(4, 30, 00) #time to trigger qotd


##reports to console when bot is primed and ready
@bot.event
async def on_ready() -> None:
  print(f"Logged in as {bot.user.name}")
  print("-----------------")

async def check_time():
    await bot.wait_until_ready()
    while True:
        general = bot.get_channel(985030405902205000)
        current_time = datetime.utcnow()
        if current_time.hour < 17: #and current_time.minute == 30:
          await general.send('working')
        await asyncio.sleep(60)

bot.loop.create_task(check_time())

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