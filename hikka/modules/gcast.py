"""
👤 USERBOT PREMIUM v2.0 | Pyrogram Hikka | Railway Ready
"""

import asyncio
import logging
import random
from datetime import datetime, timedelta

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatAdminRequired, UserPrivacyRestricted
from pyrogram.types import Message

from hikkatl.types import InlineQueryResultArticle, InputTextMessageContent
import hikkatl
from hikkatl import loader, utils

@loader.tds
class UserBotPremium(loader.Module):
    """Userbot Premium Anti-Ban Railway Ready"""
    strings = {
        "name": "👑 UserBot Premium",
        "gcast_start": "🚀 Mulai broadcast ke <b>{}</b> chats...",
        "gcast_success": "✅ <b>{}/{} berhasil → {}</b>",
        "gcast_failed": "❌ <b>{} gagal → {}</b>",
        "gcast_done": "🎉 <b>SELESAI! {}/{} chats ✅</b>",
        "gban_add": "✅ <b>Chat <code>{}</code> ditambahkan ke exception!</b>",
        "gban_del": "✅ <b>Chat <code>{}</code> dihapus dari exception!</b>",
        "gban_list": "📋 <b>Exception Chats ({len}):</b>\n\n{}",
        "afk_on": "🛌 <b>AFK DI AKTIFKAN!</b>",
        "afk_off": "✅ <b>AFK DIMATIKAN!</b>",
        "afk_status": (
            "🛌 <b>ᴜᴘs ɢᴜʏs, ɢᴜᴇ ʟᴀɢɪ ᴀꜰᴋ!</b>\n\n"
            "💭 <i>{}</i>\n"
            "⏰ <b>sᴇʟᴀᴍᴀ: {}</b>"
        ),
        "set_afk": "✅ <b>AFK Text diupdate: {}</b>"
    }

    def __init__(self):
        self.afk = False
        self.afk_time = None
        self.afk_msg = "ɢᴜᴇ ʟᴀɢɪ ᴏꜰꜰʟɪɴᴇ ʙʀᴏ, ʙᴀʀᴋᴀʟᴜɴɢɪ ᴋᴇꜱᴀᴘᴀɴ ᴛᴜᴊᴜʜᴀɴ!"
        self.exceptions = set()
        self.last_gcast = 0

    async def client_ready(self, client):
        self.client = client

    @loader.command()
    async def gcast(self, message: Message):
        """[text] - Global broadcast anti-ban"""
        text = utils.get_args_raw(message)
        if not text:
            await utils.answer(message, self.strings["no_text"])
            return

        await utils.answer(message, self.strings["gcast_start"].format("calculating..."))
        
        success, failed = 0, 0
        async for dialog in self.client.get_dialogs():
            chat_id = dialog.chat.id
            
            # Skip exceptions & private
            if chat_id in self.exceptions or dialog.chat.type.name == "PRIVATE":
                continue

            try:
                await self.client.send_message(chat_id, text)
                success += 1
                await asyncio.sleep(random.uniform(0.5, 2.0))  # Anti-ban
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except (ChatAdminRequired, UserPrivacyRestricted):
                failed += 1
            except Exception:
                failed += 1

        await utils.answer(message, self.strings["gcast_done"].format(success, success+failed))

    @loader.command()
    async def gban(self, message: Message):
        """[-add/-rm/-list] [chat_id] - Kelola exception chats"""
        args = utils.get_args_raw(message).split()
        
        if not args:
            await self._gban_list(message)
            return

        cmd, *target = args
        chat_id = int(target[0]) if target and target[0].isdigit() else None

        if cmd == "-add" and chat_id:
            self.exceptions.add(chat_id)
            await utils.answer(message, self.strings["gban_add"].format(chat_id))
        elif cmd == "-rm" and chat_id:
            self.exceptions.discard(chat_id)
            await utils.answer(message, self.strings["gban_del"].format(chat_id))
        else:
            await self._gban_list(message)

    async def _gban_list(self, message):
        if not self.exceptions:
            return await utils.answer(message, "ℹ️ <b>Tidak ada exception!</b>")
        
        chats = "\n".join([f"• <code>{cid}</code>" for cid in list(self.exceptions)[:20]])
        await utils.answer(message, self.strings["gban_list"].format(len(self.exceptions), chats))

    @loader.command()
    async def afk(self, message: Message):
        """Aktifkan AFK mode"""
        self.afk = True
        self.afk_time = datetime.now()
        await utils.answer(message, self.strings["afk_on"])

    @loader.command()
    async def on(self, message: Message):
        """Matikan AFK"""
        self.afk = False
        await utils.answer(message, self.strings["afk_off"])

    @loader.command()
    async def setafk(self, message: Message):
        """[text] - Set AFK message"""
        text = utils.get_args_raw(message)
        if text:
            self.afk_msg = text
            await utils.answer(message, self.strings["set_afk"].format(text[:50] + "..."))
        else:
            await utils.answer(message, f"📝 <b>Saat ini:</b> <i>{self.afk_msg}</i>")

    @loader.command()
    async def afkstatus(self, message: Message):
        """Status AFK & Exceptions"""
        status = f"🛡️ <b>Status Userbot:</b>\n"
        status += f"⏰ AFK: {'✅' if self.afk else '❌'}\n"
        if self.afk:
            delta = datetime.now() - self.afk_time
            status += f"⏱️ Lama: {delta.seconds//60}m {delta.seconds%60}s\n"
        status += f"📊 Exceptions: {len(self.exceptions)} chats"
        
        await utils.answer(message, status)

    @client.on_message(filters.incoming & filters.mentioned)
    async def afk_handler(self, message: Message):
        if not self.afk:
            return
            
        delta = datetime.now() - self.afk_time
        await message.reply(self.strings["afk_status"].format(
            self.afk_msg, 
            f"{delta.seconds//60}m {delta.seconds%60}s"
        ))
