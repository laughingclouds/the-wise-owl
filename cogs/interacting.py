from discord.ext import commands


class interactions(commands.Cog):
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
    

    @commands.command(name="repeat", aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        """A simple command that repeats your input

        Parameters-

        inp: str
            The input you wish to repeat.
        """
        await ctx.send(inp)

    
    @commands.command(name="hello", aliases=['hi', 'howdy'])
    async def hello(self, ctx):
        """Command to send yourself a hello...it\'s quite obv y\'know!"""
        await ctx.send(f"Hello {ctx.author.display_name}")


def setup(bot):
    bot.add_cog(interactions(bot))