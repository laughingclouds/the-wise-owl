from discord.ext import commands


@commands.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.display_name}.")


class interacting(commands.Cog):
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


def setup(bot):
    bot.add_command(hello)
    bot.add_cog(interacting(bot))