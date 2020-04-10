from telethon import events

@borg.on(events.NewMessage(from_users="@meanyabot"))
async def handler(event):
    # check media type
    if event.audio:
    	await borg.forward_messages("@songsxd", event.message)
