__mod_name__ = "Aesthetic"
__help__ = """
• .aes <text>: Buat text aesthetic
• .fancy <text>: Fancy font generator
"""

from pyrogram import Client, filters
from pyrogram.types import Message
from hikka import loader, utils

@loader.tds
class AestheticMod(loader.Module):
    """Aesthetic Module - Clone Zelda-Ubot"""
    
    strings = {
        "name": "Aesthetic",
        "no_text": "❌ Berikan text!"
    }
    
    fonts = {
        'aesthetic': '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟',
        'fancy': '𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℍ𝔦𝔍𝔎𝔏𝔐ℕ𝔒ℙℚℝ𝕤𝕋𝕌𝕍𝕎𝕏𝕐ℤ'
    }
    
    async def aes_cmd(self, message: Message):
        """Aesthetic text"""
        text = utils.get_args_raw(message)
        if not text:
            await utils.answer(message, self.strings("no_text"))
            return
        
        result = ''.join(self.fonts['aesthetic'][ord(c.lower()) - ord('a')] if c.isalpha() else c for c in text)
        await utils.answer(message, f"**Aesthetic:**\n`{result}`")
    
    async def fancy_cmd(self, message: Message):
        """Fancy text"""
        text = utils.get_args_raw(message)
        if not text:
            await utils.answer(message, self.strings("no_text"))
            return
        
        result = ''.join(self.fonts['fancy'][ord(c.upper()) - ord('A')] if c.isalpha() else c for c in text)
        await utils.answer(message, f"**Fancy:**\n`{result}`")
