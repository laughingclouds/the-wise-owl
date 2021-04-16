# ---------- importing the important libraries --------------- #
import discord
import asyncio
from os import environ
from discord.ext import commands  # for using commands.Bot() instead of discord.Client()
  # ------------------------------------------------------------ #

  # ------------------ connection and stuff -------------------- #
TOKEN = environ.get('TOKEN')  # Get TOKEN
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='gg', intents=intents)  # connection to discord (through the command section module)
#  Note: class discord.ext.commands.Bot() is a subclass of discord.client

cog_extensions = (
	'cogs.poll',
	'cogs.interacting',
	'cogs.error_handler'
)

for extension in cog_extensions:
	bot.load_extension(extension)

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}\n{bot.user.id}\n------")  # bot.user is the 'bot'
	await bot.change_presence(activity=discord.Game("gghelp"))  # will display as "playing !help"
  # ------------------------------------------------------------ #

bot.remove_command('help')

@bot.command()
async def help(ctx):
	"""Shows the help command...lol"""
	embed = discord.Embed(colour = discord.Colour.green())
	embed.set_author(name = 'Help: \nShows this message')
	embed.add_field(name = 'info', value = 'Gives info on the bot', inline = False)
	embed.add_field(name = 'all', value = 'List of all available commands', inline = False)
	await ctx.send(embed = embed)


@bot.command()	
async def info(ctx):
	"""Gives information on the bot"""
	embed = discord.Embed(colour = discord.Colour.purple())
	embed.set_author(name = 'Info')
	embed.add_field(name = 'What is it?', value = 'A discord bot made using python for helping you keep track of your goals', inline = False)
	embed.add_field(name = 'Creator', value = 'Made by \'Hemant\'', inline = False)
	embed.add_field(name = 'Source code', value = 'I\'m sharing =_=\nYou can join the server tho:\nhttps://discord.gg/bkhkSrwvW4', inline = False)
	await ctx.send(embed = embed)


@bot.command()
async def all(ctx):	
	embed = discord.Embed(colour = discord.Colour.red())
	embed.set_author(name = 'All commands of The-goal-setting-bot')
	embed.add_field(name='help', value=help.__doc__, inline=False)
	embed.add_field(name='info', value=info.__doc__, inline=False)
	embed.add_field(name='poll', value=poll.__doc__, inline=False)
	embed.add_field(name='quickpoll', value=quickpoll.__doc__, inline=False)
	embed.add_field(name='repeat', value=do_repeat.__doc__, inline=False)
	embed.add_field(name='hello', value=hello.__doc__, inline=False)
	embed.add_field(name = 'End', value = 'We\'ll be coming with new features soon', inline = False)
	await ctx.send(embed = embed)

  # --------------- the main commands -------------------------- #

bot.run(TOKEN)
