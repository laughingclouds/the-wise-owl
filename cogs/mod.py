import discord

from .utils import checks
from .utils.types import ct
from .utils.formats import beautify
from collections import Counter
from discord.ext import commands


class Mod(commands.Cog):

    # Special methods
    def __init__(self, bot):
        self.bot: ct.botType = bot

    def __repr__(self):
        return "<cogs.Mod>"

    # Miscellanious
    async def _complex_cleanup_strategy(self, ctx, search):
        prefixes = tuple(await self.bot.get_prefix(ctx.guild))

        def check(m):
            return m.author == ctx.me or m.content.startswith(prefixes)

        deleted = await ctx.channel.purge(limit=search, check=check, before=ctx.message)
        return Counter(m.author.display_name for m in deleted)

    @commands.command(aliases=["newmembers"])
    @commands.guild_only()
    async def newusers(self, ctx, *, count=5):
        """Tells you the newest members of the server.

        This is useful to check if any suspicious members have joined.

        The count parameter can only be up to 25.
        """

        count = max(min(count, 25), 1)

        if not ctx.guild.chunked:
            await ctx.guild.chunk()

        members: list[discord.Member] = sorted(
            ctx.guild.members, key=lambda m: m.joined_at, reverse=True
        )[:count]

        embed = discord.Embed(title="New Members", colour=discord.Color.green())
        for member in members:
            body = f"Joined {beautify(member.joined_at)}\nCreated {beautify(member.created_at)}"
            embed.add_field(
                name=f"{member} (ID: {member.id})", value=body, inline=False
            )

        await ctx.send(embed=embed)
        msg = [ctx.message]
        await ctx.channel.delete_messages(msg)

    @commands.command(name="joined_at")
    @commands.guild_only()
    async def member_joined_when(self, ctx: ct.ctxType, usr: ct.memberType = None):
        """Tells you when a user joined. Gives the info of the user who invoked the command; by default"""

        NAME, JOINED_AT, CREATED_AT = (
            ctx.author,
            ctx.author.joined_at,
            ctx.author.created_at,
        )
        if type(usr) in (ct.manyUsrType, ct.usrType, ct.memberType):
            NAME, JOINED_AT, CREATED_AT = usr.name, usr.joined_at, usr.created_at

        embed = discord.Embed(title=f"{NAME} joined at", colour=discord.Colour.red())
        embed.add_field(
            name=NAME,
            value=f"{beautify(JOINED_AT)}\nCreated ID at: {beautify(CREATED_AT)}",
        )
        await ctx.send(embed=embed)

    @commands.command()
    @checks.has_permissions(manage_messages=True)
    async def cleanup(self, ctx, search=100):
        """Cleans up the bots messages from the channel.
        If a search number is specified, it searches that many messages to delete.
        If the bot has Manage Messages permissions then it will try to delete
        messages that look like they invoked the bot as well.

        After the cleanup is completed, the bot will send you a message with
        which people got their messages deleted and their count. This is useful
        to see which users are spammers.

        You must have Manage Messages permission to use this.
        """

        strategy = self._complex_cleanup_strategy

        spammers = await strategy(ctx, search)  # spammers is a dictionary
        deleted = sum(spammers.values())
        add_str = " was" if deleted == 1 else "s were"
        messages = [f"{deleted} message{add_str} removed."]
        if deleted:
            messages.append("")
            spammers = sorted(spammers.items(), key=lambda t: t[1], reverse=True)
            messages.extend(f"- **{author}:** {count}" for author, count in spammers)

        await ctx.send("\n".join(messages), delete_after=5)
        await ctx.channel.delete_messages([ctx.message])

    @commands.command()
    @checks.has_permissions(manage_messages=True, read_message_history=True)
    async def clear(self, ctx: ct.ctxType, amount: int = 0):
        """Clears the given number of messages."""
        if amount == 0:
            await ctx.send("Please enter the number of messages to delete.")
            return
        messages: list = await ctx.history(limit=amount).flatten()
        await ctx.channel.delete_messages(messages)


def setup(bot: commands.Bot):
    bot.add_cog(Mod(bot))
