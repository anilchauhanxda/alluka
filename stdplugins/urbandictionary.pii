"""Urban Dictionary V2.0 
For all user
Syntax: .mean Query
Made by @meanii 
Please Don't remove credit name 
"""

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="mean?(.*)"))
@borg.on(events.NewMessage(pattern=r"\.mean?(.*)",incoming=True))

async def _(event):
    if event.fwd_from:
        return 
    await event.delete()
    process = await event.reply("```Processing...```")
    await process.delete()
    chat = "@UrbanDictionaryBot"
    meanii = event.pattern_match.group(1)

    async with borg.conversation("@UrbanDictionaryBot") as conv:
          try:    
              #mtlb = event.pattern_match.group(1)
              #await silently_send_message(conv, meanii)
              #await asyncio.sleep(1)
              #await silently_send_message(conv, meanii) 
              response = conv.wait_event(events.NewMessage(from_users=185693644))
              await event.client.send_message(chat, meanii)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock thiz bot (@UrbanDictionaryBot)```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```Can you kindly disable your forward privacy settings for good?```")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)



async def silently_send_message(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response   
