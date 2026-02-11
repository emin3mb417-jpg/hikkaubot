__mod_name__ = "Ping"
__help__ = """
• .ping: Cek ping bot
• .alive: Status bot
"""

import time
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils

@loader.tds
class PingMod(loader.Module):
    """Ping Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "Ping",
        "pong": "🏓 **Pong!**\n`{} ms`",
        "alive": "✅ **Bot Alive!**\n`Hikka Userbot Active`"
    }
    
    async def ping_cmd(self, message: Message):
        """Cek ping"""
        start = time.time()
        await message.edit("🏓 Pinging...")
        end = time.time()
        await utils.answer(message, self.strings("pong").format(int((end - start) * 1000)))
    
    async def alive_cmd(self, message: Message):
        """Status bot"""
        await utils.answer(message, self.strings("alive"))
