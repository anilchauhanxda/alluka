from telethon import events

@borg.on(events.NewMessage(chats=-1001128441021))
async def handler(event):
    
    
    	await borg.forward_messages("@meanyabot", event.message)
