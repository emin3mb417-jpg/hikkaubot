# Meta module for Hikka (aesthetic)
__meta_name__ = "Aesthetic"
__meta_help__ = """
• .aes <text>: Aesthetic text
• .fancy <text>: Fancy font
"""

from .. import loader, utils

@loader.tds
class Aesthetic(loader.Module):
    """Aesthetic Text - Fixed Hikka"""
    
    strings = {"name": "Aesthetic"}
    
    mapping = {
        'aesthetic': '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟',
        'fancy': '𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ'
    }
    
    async def aescmd(self, message):
        """Aesthetic text"""
        text = utils.get_args_raw(message)
        if not text:
            await utils.answer(message, "• Kasih text!")
            return
        
        result = ''.join(
            self.mapping['aesthetic'][ord(c.lower()) - ord('a')] 
            if c.isalpha() else c for c in text
        )
        await utils.answer(message, f"**𝔸𝕖𝕤𝕥𝕙𝕖𝕥𝕚𝕔:**\n`{result}`")
    
    async fancycmd(self, message):
        """Fancy text"""
        text = utils.get_args_raw(message)
        if not text:
            await utils.answer(message, "• Kasih text!")
            return
        
        result = ''.join(
            self.mapping['fancy'][ord(c.upper()) - ord('A')] 
            if c.isalpha() else c for c in text
        )
        await utils.answer(message, f"**𝔽𝕒𝕟𝕔𝕪:**\n`{result}`")
