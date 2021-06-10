"""`Custom Type` A module for creating type aliases for the different objects in discord.py"""

from datetime import datetime
import discord
from discord.abc import Messageable
from discord.channel import DMChannel, GroupChannel, TextChannel
from discord.ext import commands
from typing import Union


ctxType = commands.Context
clientUsrType = discord.ClientUser
datetimeType = datetime
messageableType = Union[Messageable]
memberType = discord.Member
msgType = discord.Message
usrType = discord.User

botType = commands.Bot
manyUsrType = Union[memberType, usrType]
authorType = Union[memberType, clientUsrType]