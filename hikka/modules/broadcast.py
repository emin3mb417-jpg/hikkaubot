# Meta module for Hikka (broadcast)
__meta_name__ = "Broadcast"
__meta_help__ = """
• .bc <text>: Broadcast ke semua chats
• .gcast <text>: Global cast ke groups
"""

from .. import loader, utils
import asyncio

@loader.tds
class Broadcast(loader.Module):
    """Broadcast - Fixed Hikka"""
    
    strings = {"name": "Broadcast"}
    
    async def bccmd(self, message):
        """Broadcast semua chats"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "• Kasih pesan bro!")
            return
        
        await utils.answer(message, "📢 Broadcasting...")
        
        success, failed = 0, 0
        async for dialog in self.client.iter_dialogs():
            try:
                await self.client.send_message(dialog.chat_id, args)
                success += 1
                await asyncio.sleep(0.1)
            except:
                failed += 1
        
        await utils.answer(message, f"✅ **Success:** {success}\n❌ **Failed:** {failed}")
    
    async def gcastcmd(self, message):
        """Global cast groups only"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, "• Kasih pesan!")
            return
        
        await utils.answer(message, "🌍 Gcasting...")
        
        success = 0
        async for dialog in self.client.iter_dialogs():
            if dialog.chat.type in ("group", "supergroup", "channel"):
                try:
                    await self.client.send_message(dialog.chat_id, args)
                    success += 1
                    await asyncio.sleep(0.2)
                except:
                    continue
        
        await utils.answer(message, f"✅ **GCast Success:** {success}")
