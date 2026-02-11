__mod_name__ = "Broadcast"
__help__ = """
• .broadcast <text>: Kirim pesan ke semua chat
• .gcast <text>: Global broadcast ke semua chat
"""

import asyncio
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils

@loader.tds
class BroadcastMod(loader.Module):
    """Broadcast Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "Broadcast",
        "broadcasting": "📢 Sedang broadcasting...",
        "sent_to": "✅ Terkirim ke {} chat",
        "cancelled": "❌ Dibatalkan",
        "error": "❌ Error: {}"
    }
    
    async def broadcast_cmd(self, message: Message):
        """Broadcast pesan ke semua chat"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "• Berikan pesan untuk di broadcast!")
            return
        
        await utils.answer(message, self.strings("broadcasting"))
        
        success = 0
        failed = 0
        
        async for dialog in self.client.get_dialogs():
            try:
                await self.client.send_message(dialog.chat.id, args)
                success += 1
                await asyncio.sleep(0.1)
            except Exception:
                failed += 1
        
        await utils.answer(
            message, 
            self.strings("sent_to").format(success)
        )
    
    async def gcast_cmd(self, message: Message):
        """Global cast ke semua chat"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "• Berikan pesan!")
            return
        
        await utils.answer(message, "🌍 Global broadcast dimulai...")
        # Sama seperti broadcast tapi dengan delay lebih panjang
        success = 0
        
        async for dialog in self.client.get_dialogs():
            if dialog.chat.type in ["group", "supergroup", "channel"]:
                try:
                    await self.client.send_message(dialog.chat.id, args)
                    success += 1
                    await asyncio.sleep(0.5)
                except:
                    pass
        
        await utils.answer(message, f"✅ Berhasil kirim ke {success} chats")
