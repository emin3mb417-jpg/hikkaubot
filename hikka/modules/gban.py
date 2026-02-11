__mod_name__ = "Global Ban"
__help__ = """
• .gban <reply/userid>: Global ban user
• .ungban <reply/userid>: Hapus global ban
• .gbans: List global banned users
"""

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils
import json
import os

@loader.tds
class GBanMod(loader.Module):
    """Global Ban Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "GBan",
        "gbanned": "👻 {} sudah GBanned!",
        "not_gbanned": "😭 {} tidak GBanned!",
        "ungbanned": "✅ {} dihapus dari GBan!",
        "no_gbans": "📭 Belum ada GBanned users",
        "gbanning": "⛔ Global banning...",
        "ungbanning": "✅ Meng-unban..."
    }
    
    def __init__(self):
        self.gbans_file = self.config["GBANS_FILE"] or "gbans.json"
        self.gbans = self._load_gbans()
    
    def _load_gbans(self):
        try:
            with open(self.gbans_file, 'r') as f:
                return set(json.load(f))
        except:
            return set()
    
    def _save_gbans(self):
        with open(self.gbans_file, 'w') as f:
            json.dump(list(self.gbans), f)
    
    async def gban_cmd(self, message: Message):
        """Global ban user"""
        user = await self.client.resolve_peer(message.reply_to_message.from_user.id if message.reply_to_message else utils.get_args_raw(message))
        
        await utils.answer(message, self.strings("gbanning"))
        
        self.gbans.add(user.id)
        self._save_gbans()
        
        await utils.answer(message, self.strings("gbanned").format(user.first_name))
    
    async def ungban_cmd(self, message: Message):
        """Un-global ban user"""
        user = await self.client.resolve_peer(message.reply_to_message.from_user.id if message.reply_to_message else utils.get_args_raw(message))
        
        if user.id not in self.gbans:
            await utils.answer(message, self.strings("not_gbanned").format(user.first_name))
            return
        
        self.gbans.remove(user.id)
        self._save_gbans()
        await utils.answer(message, self.strings("ungbanned").format(user.first_name))
    
    async def gbans_cmd(self, message: Message):
        """List GBanned users"""
        if not self.gbans:
            await utils.answer(message, self.strings("no_gbans"))
            return
        
        text = "👥 **GBanned Users:**\n\n"
        for uid in list(self.gbans)[:10]:  # Max 10
            try:
                user = await self.client.get_users(uid)
                text += f"• {user.first_name} (`{uid}`)\n"
            except:
                text += f"• Unknown (`{uid}`)\n"
        
        await utils.answer(message, text)
