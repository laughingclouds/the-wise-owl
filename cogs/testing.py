from discord.ext import commands


class Misc(commands.Cog):
    """For testing new bot commands without actually re-running the bot"""

    def __init__(self, bot):
        self.bot = bot
    

    @commands.command()
    async def show_all(self, ctx):
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="All commands of The Wise Owl\ngghelp <command_name> for more info on particular commands.")

        command_list = self.bot.commands

        # Adding all the commands of the bot into the embed obj
        for bot_command in command_list:
            embed.add_field(name=f'{bot_command}', value=f"{bot.command_prefix}{bot_command}", inline=False)
        embed.add_field(name='End', value='We\'ll be coming with new features soon', inline=False)

        embed.add_field(name='Field1', value="First line for Field1", inline=False)
        embed.add_field(name='', value="Second line for Field1", inline=False)
        await ctx.send(embed=embed)