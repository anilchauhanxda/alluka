"""Command: .tagall optional_text_to_tag_in
You can use it in reply to a message or directly in a new message.
  © [cHAuHaN](http://t.me/amnd33p)"""
from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd("tagall($| .*)"))
@borg.on(events.NewMessage(pattern=r"\.tagall (.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    try:
    	mentions = event.pattern_match.group(1)
    except Exception as e:
    	mentions = "..."
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        await previous_message.reply(mentions)
    else:
        await event.reply(mentions)
        await event.delete()
