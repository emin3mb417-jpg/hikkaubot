__mod_name__ = "Quotly"
__help__ = """
• .q <reply>: Buat quote
• .qpic <reply>: Quote dengan background
"""

import io
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils

@loader.tds
class QuotlyMod(loader.Module):
    """Quotly Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "Quotly",
        "generating": "🎨 Membuat quote...",
        "no_reply": "❌ Reply ke pesan!"
    }
    
    async def q_cmd(self, message: Message):
        """Buat quote text"""
        if not message.reply_to_message:
            await utils.answer(message, self.strings("no_reply"))
            return
        
        await utils.answer(message, self.strings("generating"))
        
        text = message.reply_to_message.text or message.reply_to_message.caption or "No text"
        user = await message.reply_to_message.from_user
        
        # Generate quote image (simplified)
        img = Image.new('RGB', (512, 384), color='#1a1a1a')
        d = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()
        
        # Draw text (simplified)
        d.text((20, 20), f"{user.first_name}: {text[:100]}...", fill="white", font=font)
        
        bio = io.BytesIO()
        bio.name = "quote.png"
        img.save(bio, 'PNG')
        bio.seek(0)
        
        await self.client.send_photo(message.chat.id, bio)
        await message.delete()
    
    async def qpic_cmd(self, message: Message):
        """Quote dengan background"""
        if not message.reply_to_message:
            await utils.answer(message, self.strings("no_reply"))
            return
        
        await utils.answer(message, self.strings("generating"))
        # Kirim foto original sebagai quote sederhana
        await self.client.forward_messages(
            message.chat.id,
            message.reply_to_message.chat.id,
            message.reply_to_message.id
        )
        await message.delete()
