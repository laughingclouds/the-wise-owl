import discord
from discord.ext import commands


class Misc(commands.Cog):
    """For testing new bot commands without actually re-running the bot"""

    def __init__(self, bot):
        self.bot: commands.Bot = bot

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


def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
