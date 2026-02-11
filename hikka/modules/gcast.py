__mod_name__ = "Global Cast"
__help__ = """
• .gcast <text>: Kirim ke semua groups/channels
• .gcastpic <reply photo>: Kirim foto ke semua groups
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils
import asyncio

@loader.tds
class GCastMod(loader.Module):
    """Global Cast Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "GCast",
        "casting": "🌍 Global casting...",
        "sent": "✅ Terkirim ke {} chats",
        "cancel": "❌ Dibatalkan"
    }
    
    async def gcast_cmd(self, message: Message):
        """Global cast ke groups/channels"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "• Berikan pesan!")
            return
        
        await utils.answer(message, self.strings("casting"))
        
        success = 0
        async for dialog in self.client.get_dialogs():
            if dialog.chat.type in ["group", "supergroup", "channel"]:
                try:
                    await self.client.send_message(dialog.chat.id, args)
                    success += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
        
        await utils.answer(message, self.strings("sent").format(success))
    
    async def gcastpic_cmd(self, message: Message):
        """Global cast photo"""
        if not message.reply_to_message or not message.reply_to_message.photo:
            await utils.answer(message, "• Reply ke foto!")
            return
        
        await utils.answer(message, self.strings("casting"))
        
        success = 0
        photo = message.reply_to_message.photo
        
        async for dialog in self.client.get_dialogs():
            if dialog.chat.type in ["group", "supergroup", "channel"]:
                try:
                    await self.client.send_photo(dialog.chat.id, photo.file_id)
                    success += 1
                    await asyncio.sleep(0.5)
                except:
                    pass
        
        await utils.answer(message, self.strings("sent").format(success))
