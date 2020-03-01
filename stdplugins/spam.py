from asyncio import wait

from telethon import events

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern=r"spam", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])

        await wait(
            [e.respond(spam_message) for i in range(counter)]
            )

        await e.delete()
        if LOGGER:
            await e.client.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )
