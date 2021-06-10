from os import environ
import discord
# for using commands.Bot() instead of discord.Client()
from discord.ext import commands


TOKEN = environ['TOKEN']  # Get TOKEN
intents = discord.Intents.all()
intents.members = True
# connection to discord (through the command section module)
bot = commands.Bot(command_prefix='gg', intents=intents)
#  Note: class discord.ext.commands.Bot() is a subclass of discord.client

cog_extensions = (
    'cogs.owner',
    'cogs.interacting',
    'cogs.error_handler'
) # Going with the three most important and basic cogs
# They define the skeleton/al of the bot

for extension in cog_extensions:
    bot.load_extension(extension)


@bot.event
async def on_ready():
    # bot.user is the 'bot'
    print(f"Logged in as {bot.user}\n{bot.user.id}\n------")
    # will display as "playing !help"
    await bot.change_presence(activity=discord.Game(f"{bot.command_prefix}help"))


@bot.command()
async def info(ctx):
    """Gives information on the bot"""
    embed = discord.Embed(colour=discord.Colour.purple())
    embed.set_author(name="Info")
    embed.add_field(name="What is it?",
                    value="A discord bot made using python for helping you keep track of your goals", inline=False)
    embed.add_field(
        name="Creator", value="Made by \'LaughingOutClouds\'", inline=False)
    embed.add_field(name="Source code",
                    value="I\'m not sharing =_=\nYou can join the server tho:\nhttps://discord.gg/Gu4mVGhwWJ", inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)
