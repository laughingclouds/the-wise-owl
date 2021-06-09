import discord
from discord.ext import commands
from .utils.types import ct
from googlesearch import search

class Misc(commands.Cog):
    """For testing new bot commands without actually re-running the bot"""

    def __init__(self, bot):
        self.bot: ct.botType = bot

    @commands.command()
    async def all(self, ctx):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(
            name=f"All commands of The Wise Owl\n{self.bot.command_prefix}help <command_name> for more info on particular commands.")

        command_list = self.bot.commands
        for bot_command in command_list:
            embed.add_field(
                name=f'{bot_command}', value=f"{self.bot.command_prefix}{bot_command}", inline=False)

        embed.add_field(
            name='End', value="We\'ll come back with more features soon", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name='search')
    async def do_search(self, ctx: ct.ctxType, *, searchStr: str):
        """A command that does a google search for you and returns the top 5 search results."""

        embed = discord.Embed(title='Search Results', type='link', colour=discord.Color.dark_blue())
        
        for j in search(searchStr, tld='com', num=5, stop=5, pause=2):
            embed.add_field(name='Link', value=j, inline=False)
        await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
