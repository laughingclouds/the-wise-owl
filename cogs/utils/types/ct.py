"""`Custom Type` A module for creating type aliases for the different objects in discord.py"""

from datetime import datetime
import discord
from discord.abc import Messageable
from discord.channel import DMChannel, GroupChannel, TextChannel
from discord.ext import commands
from typing import Union


ctxType = commands.Context
datetimeType = datetime
messageableType = Union[Messageable]
memberType = discord.Member
usrType = discord.User

manyUsrType = Union[memberType, usrType]
botType = commands.Bot