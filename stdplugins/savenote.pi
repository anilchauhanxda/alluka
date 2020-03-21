"""Note 
Syntax: .save with reply  message + <NoteName>
Made by @meanii 
Please Don't remove credit name 
"""

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from telethon.utils import pack_bot_file_id


@borg.on(admin_cmd(pattern="save ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return 
    if event.reply_to_msg_id:
       notename = event.pattern_match.group(1)
       chat = await event.get_input_chat()
       reply_message = await event.get_reply_message() 
       #if reply_message.media:
       #bot_api_file_id = pack_bot_file_id(reply_message.media)
       #caption = 'Caption: '+ notename + '\nFrom Chat ID: ' + str(event.chat_id) + '\nFrom User ID: ' + str(reply_message.from_id) + '\nFile ID: ' + bot_api_file_id
       #else:    
       #meanii = 'Caption: '+ notename + '\nFrom Chat ID: ' + str(event.chat_id) + '\nFrom User ID: ' + str(reply_message.from_id)
       info = "Caption 👨🏻‍💻  `{}`\nFrom Chat ID 👉🏻 `{}`\nFrom User ID 👉🏻 `{}`".format(notename,str(event.chat_id),str(reply_message.from_id))
      
       # notename = event.pattern_match.group(1)
       #reply_message = await event.get_reply_message() 
    
     
    chat =-1001337955406     #change you private group id to store notes
    sender = reply_message.sender
    await event.delete()
    processing = await event.reply("```Processing...```")
    await processing.edit("Note `{}` saved successfully 📝\nYour note Source from this user ID 👉🏻 `{}`".format(notename,str(reply_message.from_id)))
    
    async with borg.conversation(chat) as conv:
          try:     
             
              await event.client.send_message(chat, reply_message)
              await event.client.send_message(chat, info)
              
              
          except YouBlockedUserError: 
              await event.reply("```Private Group is not FOUND!!```")
              return
         
