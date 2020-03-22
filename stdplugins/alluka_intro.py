
import asyncio
import json
from telethon import events
from telethon.tl import functions, types
from sql_helpers.pmpermit_sql import is_approved, approve, disapprove, get_all_approved
from uniborg.util import admin_cmd


borg.storage.PM_WARNS = {}
borg.storage.PREV_REPLY_MESSAGE = {}


BAALAJI_TG_USER_BOT = "Tap on this 👉🏻`*alluka zoldyck` and paste it."
TG_COMPANION_USER_BOT = "Please wait!! tap on this 👉🏻`*alluka zoldyck` and paste it."
UNIBORG_USER_BOT_WARN_ZERO = "You are Spamming here, So you are blocked by me. \nNow wait, Until my Master Unblocks you." 
UNIBORG_USER_BOT_NO_WARN = "Haye, You are human!?🧐 \n If you are send me `*alluka zoldyck`\n⚠️If you are trying too much times you may be block by me.\n ☝🏻 One tip for you tap on this 👉🏻'`*alluka zoldyck`' to copy."



@borg.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    current_message_text = event.message.message.lower()
    if current_message_text == BAALAJI_TG_USER_BOT or \
        current_message_text == TG_COMPANION_USER_BOT or \
        current_message_text == UNIBORG_USER_BOT_NO_WARN:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if Config.NO_P_M_SPAM and not sender.bot:
        chat = await event.get_chat()
        if not is_approved(chat.id) and chat.id != borg.uid:
            logger.info(chat.stringify())
            logger.info(borg.storage.PM_WARNS)
            if chat.id not in borg.storage.PM_WARNS:
                borg.storage.PM_WARNS.update({chat.id: 0})
            if borg.storage.PM_WARNS[chat.id] == Config.MAX_FLOOD_IN_P_M_s:
                r = await event.reply(UNIBORG_USER_BOT_WARN_ZERO)
                await asyncio.sleep(3)
                await borg(functions.contacts.BlockRequest(chat.id))
                if chat.id in borg.storage.PREV_REPLY_MESSAGE:
                    await borg.storage.PREV_REPLY_MESSAGE[chat.id].delete()
                borg.storage.PREV_REPLY_MESSAGE[chat.id] = r
                return
            r = await event.reply(UNIBORG_USER_BOT_NO_WARN)
            borg.storage.PM_WARNS[chat.id] += 1
            if chat.id in borg.storage.PREV_REPLY_MESSAGE:
                await borg.storage.PREV_REPLY_MESSAGE[chat.id].delete()
            borg.storage.PREV_REPLY_MESSAGE[chat.id] = r


@borg.on(admin_cmd("*alluka ?(.*)"))
@borg.on(events.NewMessage(pattern=r"\*alluka  ?(.*)",incoming=True))
async def approve_p_m(event):
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    chat = await event.get_chat()
    if Config.NO_P_M_SPAM:
        if event.is_private:
            if not is_approved(chat.id):
                if chat.id in borg.storage.PM_WARNS:
                    del borg.storage.PM_WARNS[chat.id]
                if chat.id in borg.storage.PREV_REPLY_MESSAGE:
                    await borg.storage.PREV_REPLY_MESSAGE[chat.id].delete()
                    del borg.storage.PREV_REPLY_MESSAGE[chat.id]
                approve(chat.id, reason)
                await event.reply("Haye, I'm **αℓℓυкα Zᴏʟᴅʏᴄᴋ™** 👨🏻‍💻\nTo get more info about me `*info` and for help `*help`")
                await asyncio.sleep(3)
                await event.delete()


