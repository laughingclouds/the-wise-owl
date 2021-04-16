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

@bot.command()	
async def info(ctx):
	"""Gives information on the bot"""
	embed = discord.Embed(colour = discord.Colour.purple())
	embed.set_author(name = "Info")
	embed.add_field(name = "What is it?", value = "A discord bot made using python for helping you keep track of your goals", inline = False)
	embed.add_field(name = "Creator", value = "Made by \'Hemant\' aka \'LaughingOutClouds\'", inline = False)
	embed.add_field(name = "Source code", value = "I\'m not sharing =_=\nYou can join the server tho:\nhttps://discord.gg/Gu4mVGhwWJ", inline = False)
	await ctx.send(embed = embed)


@bot.command()
async def all(ctx):
	"""Shows list of all available commands"""
	embed = discord.Embed(colour = discord.Colour.red())
	embed.set_author(name = "All commands of The Wise Owl\ngghelp <command_name> for more info on particular commands.")

	command_list = bot.commands

	# Adding all the commands of the bot into the embed obj
	for bot_command in command_list:
		embed.add_field(name=f'{bot_command}', value=f"{bot.command_prefix}{bot_command}", inline=False)		
	embed.add_field(name = 'End', value = 'We\'ll be coming with new features soon', inline = False)

	await ctx.send(embed = embed)


bot.run(TOKEN)
