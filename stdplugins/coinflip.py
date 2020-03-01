"""CoinFlip for @UniBorg
Syntax: .coinflip [optional_choice]"""
from telethon import events
import random, re
from uniborg.util import admin_cmd


@borg.on(admin_cmd("coinflip ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "heads":
            await borg.send_message(event.chat_id, "The coin landed on: **Heads**. \n You were correct.")
        elif input_str == "tails":
            await borg.send_message(event.chat_id, "The coin landed on: **Heads**. \n You weren't correct, try again ...")
        else:
            await borg.send_message(event.chat_id, "The coin landed on: **Heads**.")
    elif r % 2 == 0:
        if input_str == "tails":
            await borg.send_message(event.chat_id, "The coin landed on: **Tails**. \n You were correct.")
        elif input_str == "heads":
            await borg.send_message(event.chat_id, "The coin landed on: **Tails**. \n You weren't correct, try again ...")
        else:
            await borg.send_message(event.chat_id, "The coin landed on: **Tails**.")
    else:
        await borg.send_message(event.chat_id, "¯\_(ツ)_/¯")
