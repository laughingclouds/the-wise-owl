"""`Custom Type` A module for creating type aliases for the different objects in discord.py"""

from datetime import datetime
import discord
from discord.abc import Messageable
from discord.channel import DMChannel, GroupChannel, TextChannel
from discord.ext.commands import Context
from typing import Union


datetimeType = datetime
ctxType = Context
messageableType = Union[Messageable]
usrType = discord.User
memberType = discord.Member
manyUsrType = Union[memberType, usrType]
