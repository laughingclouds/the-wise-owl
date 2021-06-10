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
    
    @commands.command(name='av', aliases=['avatar'])
    async def send_avatar(self, ctx: ct.ctxType, usr: ct.memberType=None):
        """Returns an image embed with the avatar of the command issuer by default. If a username is given or a user is mentioned, it will return that users avatar."""
        avatar_link = ctx.author.avatar.url
        if type(usr) in (ct.manyUsrType, ct.usrType, ct.memberType):
            avatar_link = usr.avatar.url

        embed = discord.Embed(color=discord.Colour.red())
        embed.set_image(url=avatar_link)
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.reply(embed=embed)
    
    @commands.command(name='snipe_copy')
    async def do_snipe(self, ctx: ct.ctxType):
        msgs_iterable = await ctx.history().flatten()
        msgs: list[discord.Message] = []
        
        for msg in msgs_iterable:
            msgs.append(msg)
        # Create an event that stores the channel id and the last deleted
        # msg in that channel.
    
    @commands.command(name='embed')
    async def sample_embed(self, ctx: ct.ctxType):
        """Just a random command that shows you how complex embeds can be."""
        embed = discord.Embed(
            title='Sample Embed',
            url='https://youtu.be/dQw4w9WgXcQ',
            description='This is a sample embed.',
            colour=discord.Colour.dark_blue()
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)

        embed.set_thumbnail(url=ctx.author.avatar.url)

        embed.add_field(name='Field1', value='Value under Field1, inline=False', inline=False)
        embed.add_field(name='Field2', value='Value under Field2, inline=True', inline=True)
        embed.add_field(name='Field3', value='Value under Field3, inline=True', inline=True)

        embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar.url)

        await ctx.reply(embed=embed)

def setup(bot: ct.botType):
    bot.add_cog(Misc(bot))
