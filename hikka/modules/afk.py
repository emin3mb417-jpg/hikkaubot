__mod_name__ = "AFK"
__help__ = """
• .afk <reason>: Set AFK
• Bot auto reply saat AFK
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils
import asyncio

@loader.tds
class AFKMod(loader.Module):
    """AFK Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "AFK",
        "afk_set": "😴 AFK di set: {}",
        "afk_reply": "💤 Saya sedang AFK\nReason: {}"
    }
    
    afk_status = False
    afk_reason = ""
    
    async def afk_cmd(self, message: Message):
        """Set AFK"""
        self.afk_status = True
        self.afk_reason = utils.get_args_raw(message) or "No reason"
        
        await utils.answer(message, self.strings("afk_set").format(self.afk_reason))
    
    async def watcher(self, message: Message):
        """Auto reply AFK"""
        if not self.afk_status or message.from_user.is_self:
            return
        
        await message.reply(self.strings("afk_reply").format(self.afk_reason))
