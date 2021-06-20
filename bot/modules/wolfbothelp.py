import datetime
import re

import aiohttp
from bs4 import BeautifulSoup
from telethon.tl.types import DocumentAttributeFilename

from .. import bot
from ..handlers.commandhandler import CommandHandler


@CommandHandler.handler(
    command="WolfBotHelp", prefixes=['!', '/', '#'],
    chats=[-1001246820081, -1001362482317, -1001173851829, -1001289165491, -1001390067401, -1001198165933, -1001319484169, -1001366720969])
async def get_nightly(event):
    """about wolf help"""
    reply = await event.reply("""🔥Wolfuserbot support group 

⚡️Rules :- @WolfRules

⚡️Channel :- @WolfUpdates

⚡️Repo :- https://github.com/MrSammyXD/Wolfuserbot

⚡️Generate string : https://repl.it/@MrSammyXD/Wolfuserbot#main.py """)
    chat = await event.get_chat()
    if chat.id == 319484169:
        await reply.delete()

__HELP__ = """\n• __`WolfBotHelp` - something about wolf bot help group__"""
