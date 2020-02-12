"""
.ft (any emoji) 
For all USER
"""

from uniborg import util
from telethon import events
from uniborg.util import admin_cmd
@borg.on(events.NewMessage(pattern=r"\.ft ? (.*)",incoming=True))
@borg.on(util.admin_cmd(pattern="ft ?(.*)"))
async def payf(event):
    paytext=event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
    await event.reply(pay)
