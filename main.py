# ---------- importing the important libraries --------------- #
import discord
import asyncio
from os import getenv
from os import environ
from dotenv import load_dotenv
from discord.ext import commands  # for using commands.Bot() instead of discord.Client()
  # ------------------------------------------------------------ #

  # ------------------ connection and stuff -------------------- #
TOKEN = environ.get('TOKEN')  # Get TOKEN
ID = int(environ.get('ID'))
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='gg', intents=intents)  # connection to discord (through the command section module)
#  Note: class discord.ext.commands.Bot() is a subclass of discord.client

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}\n{bot.user.id}\n------")  # bot.user is the 'bot'
	await bot.change_presence(activity=discord.Game("gghelp"))  # will display as "playing !help"
  # ------------------------------------------------------------ #

bot.remove_command('help')

@bot.command()
async def help(ctx):
	embed = discord.Embed(colour = discord.Colour.green())
	embed.set_author(name = 'Help: \nShows this message')
	embed.add_field(name = 'info', value = 'Gives info on the bot', inline = False)
	embed.add_field(name = 'all', value = 'List of all available commands', inline = False)
	await ctx.send(embed = embed)


@bot.command()	
async def info(ctx):
	embed = discord.Embed(colour = discord.Colour.purple())
	embed.set_author(name = 'Info')
	embed.add_field(name = 'What is it?', value = 'A discord bot made using python for helping you keep track of your goals', inline = False)
	embed.add_field(name = 'Creator', value = 'Made by \'Hemant\'', inline = False)
	embed.add_field(name = 'Source code', value = 'https://github.com/r3a10god/The-goal-setting-bot', inline = False)
	await ctx.send(embed = embed)


@bot.command()
async def all(ctx):	
	embed = discord.Embed(colour = discord.Colour.red())
	embed.set_author(name = 'All commands of The-goal-setting-bot')
	embed.add_field(name = 'reg', value = '''Register your goal and the time period with this command.
    	Format:
    	ggreg <day(00) hour(00) month(00) sec(00)> <message>''', inline = False)
	embed.add_field(name = 'End', value = 'We\'ll be coming with new features soon', inline = False)
	await ctx.send(embed = embed)

  # --------------- the main commands -------------------------- #

bot.run(TOKEN)
