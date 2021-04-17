import discord
from discord.ext import commands


class Misc(commands.Cog):
    """For testing new bot commands without actually re-running the bot"""

    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command()
    async def all(self, ctx):
        """Shows list of all available commands"""
        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(name="All commands of The Wise Owl\ngghelp <command_name> for more info on particular commands.")

        command_list = self.commands

        # Adding all the commands of the bot into the embed obj
        for bot_command in command_list:
            embed.add_field(name=f'{bot_command}', value=f"{bot.command_prefix}{bot_command}", inline=False)
        embed.add_field(name='End', value='We\'ll be coming with new features soon', inline=False)

        await ctx.send(embed=embed)


    @commands.command()
    @commands.guild_only()
    async def spoll(self, ctx, *, question):
        """Interactively creates a poll with the following question.

        To vote, use reactions!
        """

        # a list of messages to delete when we're all done
        messages = [ctx.message]
        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and len(m.content) <= 100

        for i in range(20):
            messages.append(await ctx.send(f'Say poll option or {ctx.prefix}cancel to publish poll.'))

            try:
                entry = await self.bot.wait_for('message', check=check, timeout=60.0)
            except asyncio.TimeoutError:
                break

            messages.append(entry)

            if entry.clean_content.startswith(f'{ctx.prefix}cancel'):
                break

            answers.append((to_emoji(i), entry.clean_content))

        try:
            await ctx.channel.delete_messages(messages)
        except:
            pass  # exception handling at its best

        answer = '\n'.join(f'{keycap}: {content}' for keycap, content in answers)
        actual_poll = await ctx.send(f'{ctx.author} asks: {question}\n\n{answer}')
        for emoji, _ in answers:
            await actual_poll.add_reaction(emoji)

    @spoll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Missing the question.')


def setup(bot):
    bot.add_cog(Misc(bot))