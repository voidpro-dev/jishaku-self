try:
    import selfcord as discord
    from selfcord.ext import commands
except:
    import discord
    from discord.ext import commands
# -*- coding: utf-8 -*-

"""
jishaku.types
~~~~~~~~~~~~~

Declarations for type checking

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""

import typing

BotT = typing.Union[commands.Bot, None]

if typing.TYPE_CHECKING or False:
    ContextT = typing.TypeVar('ContextT', commands.Context[commands.Bot], commands.Context[commands.AutoShardedBot])
    ContextA = commands.Context[BotT]
else:
    ContextT = ContextA = commands.Context
