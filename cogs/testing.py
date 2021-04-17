from discord.ext import commands


def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)


class Misc(commands.Cog):
    """For testing new bot commands without actually re-running the bot"""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Misc(bot))