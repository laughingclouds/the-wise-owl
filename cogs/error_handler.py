import sys
import discord
import traceback
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    """An error handler for discord commands"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """This event is trigerred whern an error is raised while invoking a command.
        
        Parameters:
        ctx: commands.Context
            The context used for command invocation
        error: commands.CommandError
            The exception raised.
        """

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):

            embed = discord.Embed(colour = discord.Colour.purple())
            embed.set_author(name = 'Error lol')
            embed.add_field(name = '\'on_error\'', value = 'https://discordpy.readthedocs.io/en/latest/api.html#discord.on_error', inline = False)
            embed.add_field(name = '', value = 'This is an error for the local handlers to deal with...hopefully not me.', inline = False)
            await ctx.send(embed=embed)            
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.command.error) is not None:
                return
        
        ignored = (commands.CommandNotFound, )

        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error
        error = getattr(error, 'original', error)


        # Anything in ignored will return and prevent anything happening
        if isinstance(error, ignored):
            return
        
        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f"{ctx.command} has been disabled.")
        
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f"{ctx.command} can\'t be used in the DMs.")
            except discord.HTTPException:
                pass
        
        # check to see where it came from

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == ("poll", "quickpoll"):  # Check if the command being invoked is 'tag list'
                await ctx.send('Hey kiddo, how dumb do you need to be to enter the arguements wrong?')
        
        else:
            # All other errors not returned come here. And we can just print the default Traceback.
            msg = "There was an error, and cuz\' my creator is too lazy he didn\'t add much error handling.\nAnyways, here is the error msg:\n"
            
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_author(name='Error lol')
            embed.add_field(name='A msg for you:', value=msg, inline=False)
            embed.add_field(name=f"{type(error).__name__}", value=f"{error}", inline=False)
            try:
                await ctx.send(embed=embed)
            except:
                await ctx.send("Error lol, could u pls contact my developer at \nhttps://discord.gg/Gu4mVGhwWJ  ?")

        

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
