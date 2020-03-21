"""
Syntax:
*insult(with reply user message)
For for Users only
customized by @meanii 
Please Don't remove credit name 

"""


from telethon import events
from uniborg.util import admin_cmd
import asyncio
from telethon.tl import functions, types
import random
from sql_helpers.global_variables_sql import LOGGER, SUDO_USERS
import sys
import time


@borg.on(admin_cmd(pattern="insult ?(.*)"))
@borg.on(events.NewMessage(pattern=r"\*insult(.*)",incoming=True))
async def _(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    adjectives_start = ["salty", "fat", "f*cking", "sh*tty",
                        "stupid", "retarded", "self conscious", "tiny"]
    adjectives_mid = ["little", "vitamin D deficient",
                      "idiotic", "incredibly stupid"]
    nouns = ["cunt", "pig", "pedophile", "beta male", "bottom", "retard", "a*s licker", "cunt nugget",
             "P*NIS", "d*ckhead", "flute", "idiot", "m*therf*cker", "loner", "creep"]
    starts = ["You're a", "You", "F*ck off you", "Actually die you", "Listen up you",
              "What the f*ck is wrong with you, you"]
    ends = ["!!!!", "!", ""]
    log_insults = ""
    if args:
        pass
    else:
        args = 5
    try:
        args = int(args)
    except Exception as error:
        await event.edit(error)
    for insulting in range(args):
        start = random.choice(starts)
        adjective_start = random.choice(adjectives_start)
        adjective_mid = random.choice(adjectives_mid)
        noun = random.choice(nouns)
        end = random.choice(ends)
        insult = start + " " + adjective_start + " " + \
            adjective_mid + (" " if adjective_mid else "") + noun + end
        log_insults += f"```{insult}```\n\n"
        reply_msg = await event.get_reply_message()
        if reply_msg:
            user_id = f"```{reply_msg.from_id}```"
            noformat_userid = reply_msg.from_id
        else:
            user_id = "Unknown user"
            noformat_userid = "Unknown user"
        if noformat_userid in SUDO_USERS:
            await event.reply("**Wait! WHAT?!\nDid you just try to insult my creator?!?!\nBYE!**")
            sys.exit()
            # probably not needed but meh
            break
        else:
            await event.reply(insult)
            time.sleep(2)
        await borg.send_message(
            LOGGER,
            f"Insulted [{user_id}] with:\n\n{log_insults}"
       )
