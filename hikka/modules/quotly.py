# Meta module for Hikka (quotly - no PIL)
__meta_name__ = "Quotly"
__meta_help__ = """
• .q <reply>: Buat quote
• .qpic <reply>: Quote foto
"""

from .. import loader, utils
import asyncio

@loader.tds
class Quotly(loader.Module):
    """Quotly - Text-based quotes"""
    
    strings = {
        "name": "Quotly",
        "quote_made": "📝 Quote dibuat!",
        "no_reply": "❌ Reply ke pesan!",
        "generating": "✨ Membuat..."
    }
    
    async def qcmd(self, message):
        """Buat quote dari reply"""
        if not message.is_reply:
            await utils.answer(message, self.strings("no_reply"))
            return
        
        replied = await message.get_reply_message()
        user = await self.client.get_entity(replied.sender_id)
        
        quote_text = f"""
╔═══════❰ Quote ❱═══════╗
║ **From:** {utils.escape_html(user.first_name)}
║ **Text:** {utils.escape_html(replied.text or 'Media')}
╚═══════════════════════╝"""
        
        await utils.answer(message, self.strings("quote_made"))
        await message.reply(quote_text)
        await message.delete()
    
    async def qpiccmd(self, message):
        """Quote foto (forward only)"""
        if not message.is_reply:
            await utils.answer(message, self.strings("no_reply"))
            return
        
        await utils.answer(message, self.strings("generating"))
        await self.client.forward_messages(
            message.chat_id, 
            message.reply_to_message_id
        )
        await message.delete()
