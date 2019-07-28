import discord 
import random
from discord.ext import commands
client = commands.Bot(command_prefix = '.')
client.remove_command('help')
@client.event
async def on_ready():
    print('Bot is ready')

@client.command(aliases=['ping'])
async def bing(ctx):
    x = random.randint(1,6)
    if x == 1:
       await ctx.send (f'Pong.  ({round(client.latency * 1000)}ms)')
    if x == 2:
       await ctx.send (f'Programming is ez pz.  ({round(client.latency * 1000)}ms)')  
    if x == 3:
       await ctx.send (f'Shut it DGK my coding is good.  ({round(client.latency * 1000)}ms)') 
    if x == 4:
       await ctx.send (f'Bow down to the supreme leader.  ({round(client.latency * 1000)}ms)') 
    if x == 5:
       await ctx.send (f'Geometry Dash is harder than Osu!, Scrubs.  ({round(client.latency * 1000)}ms)') 
    if x == 6:
       await ctx.send (f'RIP Etika  ({round(client.latency * 1000)}ms)') 
@client.command()
async def help(ctx):
    await ctx.send('''
    Commands: 
    .ping - Check the latency of the bot and get some funny messages
    .help - What you're looking at right now
    .doggo - Sends a picture of a cute doggo
    .kitty - Sends a picture of a cute kity
    .info - gives info about the bot
    More coming soon!!!!''')

@client.command()
async def doggo(channel):
  y = random.randint(1,2)
  if y == 1:
      await channel.send(file=discord.File('Pictures/smh.png'))
  if y ==2:
      await channel.send(file=discord.File('Pictures/smh2.png'))

@client.command()
async def kitty(channel):
    z = random.randint(1,2)
    if z == 1:
        await channel.send(file=discord.File('Pictures/kitty.png'))
    if z == 2:
         await channel.send(file=discord.File('Pictures/kitty2.png'))

@client.command()
async def info(ctx):
      await ctx.send('''
      Made by ZizOhNo#1012
      Support Server: https://discord.gg/9AprD9p
      Started 7/27/19
      ''')


@client.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/api/oauth2/authorize?client_id=601418773874081792&permissions=8&scope=bot')


client.run('NjAxNDE4NzczODc0MDgxNzky.XTzNLw.2xWsEUCzANIF2JaMz9eoY1P9VZM')