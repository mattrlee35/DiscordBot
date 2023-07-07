import discord
import os
import emoji
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.lower().startswith('-commands'):
    await message.channel.send('-se17: Provides the SE scores from August 7th\n-se18: Provides the SE scores from August 21st\n-se19: Provides the SE scores from September 4th\n-se20: Provides the SE scores from September 19th\n-se21: Provides the SE scores from October 16th')
  if message.content.lower().startswith('-se17'):
    await message.channel.send('https://i.gyazo.com/0aaa9dd5351b9f231737d96c3f82b701.png')
  if message.content.lower().startswith('-se18'):
    await message.channel.send('https://i.gyazo.com/0addceac09bcf76e859d27386e9c85f6.png')
  if message.content.lower().startswith('-se19'):
    await message.channel.send('https://i.gyazo.com/4db91df544864338e11aa3ff8b89f46e.png')
  if message.content.lower().startswith('-se20'):
    await message.channel.send('https://i.gyazo.com/2aab5075900aa26d5639c5006034d9c6.png')
  if message.content.lower().startswith('-se21'):
    await message.channel.send('https://gyazo.com/befcca34c47701c85eeaf1903611bbf9.png')
  

keep_alive()
client.run(os.getenv('TOKEN'))