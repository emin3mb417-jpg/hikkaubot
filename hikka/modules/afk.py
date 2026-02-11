# Meta module for Hikka (afk)
__meta_name__ = "AFK"
__meta_help__ = """
• .afk <reason>: Set AFK mode
"""

from .. import loader, utils

@loader.tds
class AFK(loader.Module):
    """AFK - Fixed Hikka"""
    
    afk_mode = False
    afk_reason = ""
    
    strings = {"name": "AFK"}
    
    async def afkcmd(self, message):
        """Set AFK"""
        self.afk_mode = True
        self.afk_reason = utils.get_args_raw(message) or "No reason"
        await utils.answer(message, f"😴 **AFK:** {self.afk_reason}")
    
    async def watch(self, message):
        """AFK reply handler"""
        if not self.afk_mode or message.out or message.mentioned:
            return
        
        await message.reply(f"💤 **AFK**\n_{self.afk_reason}_")
