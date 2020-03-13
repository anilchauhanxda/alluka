import html
from telethon import events
from telethon.utils import get_display_name
from telethon.tl.types import InputPeerUser
from betray import register, DB

DB.execute("""CREATE TABLE IF NOT EXISTS IGNOREUSERS
(USERID INT UNIQUE PRIMARY KEY NOT NULL)""")
DB.commit()

def is_ignored(uid):
    return [i for i in DB.execute("SELECT USERID FROM IGNOREUSERS WHERE USERID = ?", (uid,))]

@register(events.NewMessage(outgoing=True, pattern=r'\.ignore(?:u(?:ser)?)? (?:[Tt]rue|yes|on)(?: (.+))?'))
async def ignore_true(e):
    user = e.pattern_match.group(1)
    try:
        user = int(user or 0)
    except ValueError:
        pass
    if not user:
        r = await e.get_reply_message()
        user = getattr(r, 'from_id', None)
    if not user:
        await e.edit('err \\\nNo user specified nor reply, or invalid user')
        return
    ieuser = await e.client.get_input_entity(user)
    if not isinstance(ieuser, InputPeerUser):
        await e.edit('err \\\nInvalid user')
        return
    user = int(ieuser.user_id)
    if is_ignored(user):
        await e.edit('noop \\\nUser already ignored')
        return
    DB.execute("INSERT INTO IGNOREUSERS (USERID) VALUES (?)", (user,))
    DB.commit()
    await e.edit('User ignored!')

@register(events.NewMessage(outgoing=True, pattern=r'\.ignore(?:u(?:ser)?)? (?:[Ff]alse|no|off)(?: (.+))?'))
async def ignore_false(e):
    user = e.pattern_match.group(1)
    try:
        user = int(user or 0)
    except ValueError:
        pass
    if not user:
        r = await e.get_reply_message()
        user = getattr(r, 'from_id', None)
    if not user:
        await e.edit('err \\\nNo user specified nor reply, or invalid user')
        return
    ieuser = await e.client.get_input_entity(user)
    if not isinstance(ieuser, InputPeerUser):
        await e.edit('err \\\nInvalid user')
        return
    user = ieuser.user_id
    if not is_ignored(user):
        await e.edit('noop \\\nUser not ignored')
        return
    DB.execute("DELETE FROM IGNOREUSERS WHERE USERID = ?", (user,))
    DB.commit()
    await e.edit('User un-ignored!')

@register(events.NewMessage(outgoing=True, pattern=r'\.ignore(?:u(?:sers?)?)?$'))
async def list_ignored(e):
    text = 'Type[DBGet]\n'
    await e.edit(text + 'State[Executing]')
    uids = [i[0] for i in DB.execute("SELECT USERID FROM IGNOREUSERS")]
    text += 'State[Executed]\n'
    text += 'IgnoredUsers \\\n'
    for uid in uids:
        u = await e.client.get_entity(uid)
        if u.deleted:
            DB.execute("DELETE FROM IGNOREUSERS WHERE USERID = ?", (user,))
            DB.commit()
            continue
        text += f'<a href="tg://user?id={uid}">{html.escape(get_display_name(u))}</a>\n'
    await e.edit(text)

@register(events.NewMessage(incoming=True), flags='hiddenerrors')
async def do_the_ignoring(e):
    if e.mentioned or e.is_private:
        if is_ignored(e.from_id) if e.from_id else False:
            await e.client.send_read_acknowledge(e.chat_id, [e.message], clear_mentions=True)
