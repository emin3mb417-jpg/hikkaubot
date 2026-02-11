# Meta module for Hikka (gban)
__meta_name__ = "GBan"
__meta_help__ = """
• .gban <reply/user>: Global ban
• .ungban <reply/user>: Hapus gban
• .gbans: List gbanned
"""

from .. import loader, utils
import json
import os

@loader.tds
class GBan(loader.Module):
    """Global Ban - Fixed Hikka"""
    
    strings = {"name": "GBan"}
    
    def __init__(self):
        self.config = loader.ModuleConfig(
            "GBANS_FILE", "gbans.json", 
            lambda: "Path to gbans file"
        )
        self.gbans_file = self.config["GBANS_FILE"]
        self._load_gbans()
    
    def _load_gbans(self):
        try:
            if os.path.exists(self.gbans_file):
                with open(self.gbans_file, 'r') as f:
                    self.gbans = set(json.load(f))
            else:
                self.gbans = set()
        except:
            self.gbans = set()
    
    def _save_gbans(self):
        try:
            with open(self.gbans_file, 'w') as f:
                json.dump(list(self.gbans), f)
        except:
            pass
    
    async def gbancmd(self, message):
        """Global ban user"""
        if not message.is_reply and not message.text.split(maxsplit=1)[1:]:
            await utils.answer(message, "• Reply atau kasih user ID!")
            return
        
        user_id = (await message.get_reply_message()).sender_id if message.is_reply else int(message.text.split(maxsplit=1)[1])
        
        self.gbans.add(user_id)
        self._save_gbans()
        
        await utils.answer(message, f"👻 User `{user_id}` GBanned!")
    
    async def ungbancmd(self, message):
        """Hapus gban"""
        if not message.is_reply and not message.text.split(maxsplit=1)[1:]:
            await utils.answer(message, "• Reply atau kasih user ID!")
            return
        
        user_id = (await message.get_reply_message()).sender_id if message.is_reply else int(message.text.split(maxsplit=1)[1])
        
        if user_id not in self.gbans:
            await utils.answer(message, f"😭 User `{user_id}` bukan GBanned!")
            return
        
        self.gbans.remove(user_id)
        self._save_gbans()
        await utils.answer(message, f"✅ User `{user_id}` di-unGBan!")
    
    async def gbanscmd(self, message):
        """List GBanned"""
        if not self.gbans:
            await utils.answer(message, "📭 No GBanned users")
            return
        
        text = "👥 **GBanned Users:**\n"
        for uid in list(self.gbans)[:15]:
            try:
                user = await self.client.get_entity(uid)
                text += f"• {utils.escape_html(user.first_name)} [`{uid}`]\n"
            except:
                text += f"• Unknown [`{uid}`]\n"
        
        await utils.answer(message, text)
