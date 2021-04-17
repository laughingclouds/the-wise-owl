from discord.ext import commands


class Misc(commands.Cog):
    """For testing new bot commands without actually re-running the bot"""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Misc(bot))