from discord.ext import commands


@commands.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}.")


class interacting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        msg = "G'day! If you leave I'll kill you"
        await ctx.send(msg)
    
    @commands.Cog.listener()
    async def on_member_remove(self, ctx):
        msg = "And there they go. It\'s all fun and games until Blaze bans you."
        await ctx.send(msg)



def setup(bot):
    bot.add_command(hello)
    bot.add_cog(interacting(bot))