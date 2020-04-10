from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd

@borg.on(events.NewMessage(pattern="https://?(.*)",))
async def _(event):
    if event.fwd_from:
        return
    input_str = "/music " + event.pattern_match.group(1) 
   
    send = await borg.send_message("@meanyabot", "{}".format(input_str))
       # error="undefined"
        #if send = error
        #await event.reply("Not able to Found 😕/n{} ".format(input_str))


        
