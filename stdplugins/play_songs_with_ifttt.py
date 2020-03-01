from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"play ?(.*)", allow_sudo=True))
async def test(event):
    if event.fwd_from:
        return
    uwu = event.pattern_match.group(1)
    await borg.send_message(event.chat_id, "Playing {}".format(uwu))
    await borg.send_message("@ifttt", "#play {}".format(uwu))