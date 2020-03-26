"""
.log to view bot log
For all users
"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="log"))
@borg.on(events.NewMessage(pattern=r"\.log(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = """**αℓℓυкα Zᴏʟᴅʏᴄᴋ™** //logs\n\n//8th feb 2020//\n• Fix `.kang` double reply.\n• Added new plugin `. into ur count` To view my stats 😉 **FOR SUDO USER ONLY**\n\n//10th feb 2020//\n• Added `.ai` (Your message) AI chat Bot 😉 [BUT VERY SLOW TO REPLY 😕]\n\n//11th Feb 2020//\n• Added `.slap` in reply to any message, or u gonna slap urself.\n• Added `.rnupload` file.name\n\n//12th feb 2020// \n• Added `.ft` (any emoji) 
    \n//13 March 2020//\n• Change prefix .ud to .mean \n• Added `.rrgb` Random RGB text Sticker\n• Added `.tagall` to tag all ppl in chat \n• Added `.commit` to upload plugins into ur github ripo (SUDO ONLY)
    
    //26 March 2020//
    •Added `.decide` to get ans YES or NO
    •Added `.paste`paste bin 
    •Added `.userlist` to get all users in your chat.
    •Added `.setwelcome` set welcome message in your chat.
    •Added `.clearwelcome` disbale welcome message in your chat.
  
    """
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
