from discord.ext import commands


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.on_member_join_msg = "G'day! If you leave I'll kill you"
        self.on_member_remove_msg = "And there they go. It\'s all fun and games until Blaze bans you."
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(self.on_member_join_msg)
        else:
            pass # send msg to admins to create a sys chan
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = member.guild.system_channel
        if channel is not None:
                await channel.send(self.on_member_remove_msg)
        else:
            pass # send msg to admins to create a sys chan
    

    @commands.command(name="say", aliases=['mimic', 'repeat', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        """A simple command that repeats your input

        Parameters-

        inp: str
            The input you wish to repeat.
        """
        msg = [ctx.message]  # msg to delete
        await ctx.channel.delete_messages(msg)
        await ctx.send(inp)
    
    # local error handler for the command "do_repeat"
    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.
        
        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """

        # Check if our required argument inp is missing.
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send(f"You forgot to give the input.")

    
    @commands.command(name="hello", aliases=['hi', 'howdy'])
    async def hello(self, ctx):
        """Command to send yourself a hello...it\'s quite obv y\'know!"""
        await ctx.send(f"Hello {ctx.author.display_name}")


def setup(bot):
    bot.add_cog(Interactions(bot))