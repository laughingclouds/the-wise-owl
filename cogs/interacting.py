import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import context
from .utils.types import ct
from .utils.formats import beautify
from datetime import datetime


class Interactions(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.on_member_join_msg = "G'day! If you leave I'll kill you"
        self.on_member_remove_msg = (
            "And there they go. It's all fun and games until Blaze bans you."
        )
        self.deleted_msg_dict: dict[int, tuple[ct.msgType, ct.datetimeType]] = {}

    @commands.Cog.listener()
    async def on_message_delete(self, msg: ct.msgType):
        channel = msg.channel.id
        self.deleted_msg_dict[channel] = (msg, beautify(datetime.utcnow()))
        await asyncio.sleep(60)
        try:
            del self.deleted_msg_dict[channel]
        except KeyError:
            pass

    @commands.Cog.listener()
    async def on_member_join(self, member: ct.memberType):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(self.on_member_join_msg)
        else:
            pass  # send msg to admins to create a sys chan

    @commands.Cog.listener()
    async def on_member_remove(self, member: ct.memberType):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(self.on_member_remove_msg)
        else:
            pass  # send msg to admins to create a sys chan

    @commands.command(name="say", aliases=["mimic", "repeat", "copy"])
    async def do_repeat(self, ctx: ct.ctxType, *, inp: str):
        """A simple command that repeats your input

        Parameters-

        inp: str
            The input you wish to repeat.
        """
        msg = [ctx.message]  # msg to delete
        await ctx.channel.delete_messages(msg)
        await ctx.send(inp)

    # local error handler for the command "do_repeat"
    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        """A local Error Handler for our command do_repeat.

        This will only listen for errors in do_repeat.
        The global on_command_error will still be invoked after.
        """

        # Check if our required argument inp is missing.
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == "inp":
                await ctx.send(f"You forgot to give the input.")

    @commands.command(name="hello", aliases=["hi", "howdy"])
    async def hello(self, ctx: ct.ctxType):
        """Command to send yourself a hello...it\'s quite obv y\'know!"""
        await ctx.send(f"Hello {ctx.author.display_name}")

    @commands.command(name="snipe")
    async def snipe(self, ctx: ct.ctxType):
        """Returns the `UTC` time of when a message is deleted."""
        channel = ctx.channel.id
        if channel not in self.deleted_msg_dict:
            await ctx.send("There's nothing to snipe!")
            return

        msg, delete_time = self.deleted_msg_dict[channel]
        author, icon_url = msg.author, msg.author.avatar.url
        embed = discord.Embed(type="rich", colour=discord.Colour.dark_purple())
        embed.set_author(name=author, icon_url=icon_url)
        embed.add_field(name="Message sniped", value=msg.content)
        embed.set_footer(text=f"Deleted at {delete_time}")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Interactions(bot))
