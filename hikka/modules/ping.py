# Meta module for Hikka (ping)
__meta_name__ = "Ping"
__meta_help__ = """
• .ping: Cek latency
• .al: Status alive
"""

from .. import loader, utils
import time

@loader.tds
class Ping(loader.Module):
    """Ping - Fixed Hikka"""
    
    strings = {"name": "Ping"}
    
    async def pingcmd(self, message):
        """Cek ping"""
        start = time.time()
        await message.edit("🏓...")
        end = time.time()
        ms = int((end - start) * 1000)
        await utils.answer(message, f"🏓 **Pong!** `{ms}ms`")
    
    async def alcmd(self, message):
        """Alive status"""
        await utils.answer(message, "✅ **Alive!**\n`Hikka Userbot Ready`")
