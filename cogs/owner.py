from discord.ext import commands


class OwnerCog(commands.Cog):
    """Commands that can be run by an owner only"""

    def __init__(self, bot):
        self.bot = bot
    
    # hidden: the command won't show in the default help command
    # is_owner means only the bot owner (or a team which owns the bot) will be able to use this command
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command to load a module.
        Use the dot path in this one.
        e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERORR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(f"{cog} loaded successfully")


    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command to unload a module.
        Use the dot path."""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(f"{cog} unloaded successfully")
    

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command to reload a module.
        Use the dot path."""

        try:
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send(f"{cog} reloaded successfully")


def setup(bot):
    bot.add_cog(OwnerCog(bot))
