"""Type `.df` reply to a photo or sticker
   for all user
"""
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="df ?(.*)"))
@borg.on(events.NewMessage(pattern=r"\.df ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.reply("```Reply to any user message.```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.media:
       await event.reply("```Reply to any sticker or pics to destroy..```")
       return
    chat = "@image_deepfrybot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.reply("```Reply to actual users message.```")
       return

    meanii = await event.reply("```Processing```")
    async with borg.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=432858024))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please Fak Off...```")
              return
          if response.text.startswith("Forward"):
             await event.reply("```Ur bot is sleeping now.. bye bye..```")
          else: 
             await meanii.delete()
             await event.client.send_file(event.chat_id, response.message.media)
