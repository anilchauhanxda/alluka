"""Duck Duck Go  
For all users
Syntax: .ddg Query
customized by @meanii 
Please Don't remove credit name 
"""

from telethon import events
import os
import requests
import json
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="ddk?(.*)"))
@borg.on(events.NewMessage(pattern=r"\.ddg?(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    
    input_str = event.pattern_match.group(1)
    sample_url = "https://duckduckgo.com/?q={}".format(input_str.replace(" ","+"))
    if sample_url:
        link = sample_url.rstrip()
        await event.reply("Let me 🦆 DuckDuckGo that for you:\n🔎 [{}]({})".format(input_str, link))
    else:
        await event.reply("something is wrong. please try again later.")
