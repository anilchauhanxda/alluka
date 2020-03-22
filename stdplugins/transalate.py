""" Google Translate
Available Commands:
For all users
.tr LanguageCode as reply to a message
.tr LangaugeCode | text to translate
Made by @meanii 
Please Don't remove credit name 
"""

import emoji
from telethon import events
from googletrans import Translator
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="tr ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply("`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
       
        output_str = """**TRANSLATED** from {} to {}
{}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.reply(output_str)
    except Exception as exc:
        await event.edit(str(exc))
