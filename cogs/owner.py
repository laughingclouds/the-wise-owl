from discord.ext import commands


class OwnerCog(commands.Cog):
    """Commands that can be run by an owner only"""

    def __init__(self, bot):
        self.bot: commands.Bot = bot

    # hidden: the command won't show in the default help command
    # is_owner means only the bot owner (or a team which owns the bot) will be able to use this command
    @commands.command(hidden=True)
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Command to load a module.
        Use the dot path in this one.
        e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERORR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("\N{OK HAND SIGN}")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Command to unload a module.
        Use the dot path."""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("\N{OK HAND SIGN}")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Command to reload a module.
        Use the dot path."""

        try:
            self.bot.reload_extension(cog)
        except Exception as e:
            await ctx.send(f"**`ERROR:`** {type(e).__name__} - {e}")
        else:
            await ctx.send("\N{OK HAND SIGN}")


def setup(bot: commands.Bot):
    bot.add_cog(OwnerCog(bot))
