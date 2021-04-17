import discord
import asyncio
from .utils import time, checks
from collections import Counter
from discord.ext import commands


class Mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Miscellanious
    async def _basic_cleanup_strategy(self, ctx, search):
        count = 0
        async for msg in ctx.history(limit=search, before=ctx.message):
            if msg.author == ctx.me:
                await msg.delete()
                count += 1
        return {'Bot': count}
    

    async def _complex_cleanup_strategy(self, ctx, search):
        prefixes = tuple(self.bot.get_guild_prefixes(ctx.guild))

        def check(m):
            return m.author == ctx.me or m.content.startswith(prefixes)
        
        deleted = await ctx.channel.purge(limit=search, check, before=ctx.message)
        return Counter(m.author.display_name for m in deleted)


    @commands.command(aliases=['newmembers'])
    @commands.guild_only()
    async def newusers(self, ctx, *, count=5):
        """Tells you the newest members of the server.

        This is useful to check if any suspicious members have joined.

        The count parameter can only be up to 25.
        """

        count = max(min(count, 25), 5)

        if not ctx.guild.chunked:
            await ctx.guild.chunk()
        
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at, reverse=True)[: count]

        embed = discord.Embed(title='New Members', colour=discord.Color.green())

        for member in members:
            body = f"Joined {time.human_timedelta(member.joined_at)}\nCreated {time.human_timedelta(member.created_at)}"
            embed.add_field(name=f'{member} (ID: {member.id})', value=body, inline=False)
        
        await ctx.send(embed=embed)
    

    @commands.command()
    @checks.has_permissions(manage_messages=True)
    async def clear(self, ctx, search=100):
        """Cleans up the bot's messages from the channel.
        If a search number is specified, it searches that many messages to delete.
        If the bot has Manage Messages permissions then it will try to delete
        messages that look like they invoked the bot as well.

        After the cleanup is completed, the bot will send you a message with
        which people got their messages deleted and their count. This is useful
        to see which users are spammers.

        You must have Manage Messages permission to use this.
        """

        strategy = self._basic_cleanup_strategy
        if ctx.me.permissions_in(ctx.channel).manage_messages:
            strategy = self._complex_cleanup_strategy
        
        spammers = await strategy(ctx, search)  # spammers is a dictionary
        deleted = sum(spammers.values())
        messages = [f"{deleted} message{" was" if deleted == 1 else "s were"} removed."]
        if deleted:
            message.append('')
            spammers = sorted(spammers.items(), key=lambda t: t[1], reverse=True)
            messages.extend(f"- **{author}:** {count}" for author, count in spammers)
        
        await ctx.send('\n'.join(messages), delete_after=5)