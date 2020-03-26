"""Enable Seen Counter in any message,
to know how many users have seen your message
Syntax: .letsee as reply to any message"""
from telethon import events
from uniborg.util import admin_cmd

PRIVATE_CHANNEL_BOT_API_ID = -1001263855672

@borg.on(admin_cmd(pattern="hmm"))
async def _(event):
    if event.fwd_from:
        return"""Enable Seen Counter in any message,
to know how many users have seen your message
Syntax: .letsee as reply to any message"""
from telethon import events
from uniborg.util import admin_cmd

PRIVATE_CHANNEL_BOT_API_ID = -1001263855672

@borg.on(admin_cmd(pattern="letsee"))
@borg.on(events.NewMessage(pattern=r"\.letsee(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    if PRIVATE_CHANNEL_BOT_API_ID is None:
        await event.edit("Please set the required environment variable `PRIVATE_CHANNEL_BOT_API_ID` for this plugin to work")
        return False
    try:
        e = await borg.get_entity(int(PRIVATE_CHANNEL_BOT_API_ID))
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
       
        fwd_message = await borg.forward_messages(
            e,
            re_message,
            silent=True
        )
        await borg.forward_messages(
            event.chat_id,
            fwd_message
        )
        
        await event.delete()

    if PRIVATE_CHANNEL_BOT_API_ID is None:
        await event.edit("Please set the required environment variable `PRIVATE_CHANNEL_BOT_API_ID` for this plugin to work")
        return False
    try:
        e = await borg.get_entity(int(Config.PRIVATE_CHANNEL_BOT_API_ID))
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
       
        fwd_message = await borg.forward_messages(
            e,
            re_message,
            silent=True
        )
        await borg.forward_messages(
            event.chat_id,
            fwd_message
        )
        await fwd_message.delete()
        await event.delete()
