"""ai bot
Syntax: *ai Your message
Made by @meanii 
Please Don't remove credit name 
"""

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="ai ?(.*)"))
@borg.on(events.NewMessage(pattern=r"\*ai ?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return 
    
  
    chat = "@LydiaChatBot"
    meanii = event.pattern_match.group(1)

    async with borg.conversation("@LydiaChatBot") as conv:
          try:    
              
              response = conv.wait_event(events.NewMessage(from_users=869979136))
              await event.client.send_message(chat, meanii)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock thiz bot (@allukabot)```")
              return
          if response.text.startswith(" "):
             await event.edit("I'm **αℓℓυкα Zᴏʟᴅʏᴄᴋ™** 👨🏻‍💻")
          
          
          else: 
             #await event.delete()
             await event.client.send_message(event.chat_id, response.message)

          
        


async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response   
