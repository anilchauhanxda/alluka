import io
import textwrap
import random
from telethon import events

from PIL import Image, ImageDraw, ImageFont

from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="srgb (.*)"))
@borg.on(events.NewMessage(pattern=r"\*srgb ?(.*)",incoming=True))
async def sticklet(event):
    
    R = random.randint(0,256)
    G = random.randint(0,256)
    B = random.randint(0,256)
    FC = random.randint(1,16)
    sticktext = event.pattern_match.group(1)

    if not sticktext:
        await event.edit("`I need text to sticklet!`")
        return

    await event.delete()

    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 230

    if FC==1:
      FONT_FILE = "Fonts/ActionNowPersonalUseRegular-nRvGV.ttf"
    if FC==2:
      FONT_FILE = "Fonts/AlouettePersonalUse-PKG4P.ttf"
    if FC==3:
      FONT_FILE = "Fonts/CakeNom-87Y0.ttf"
    if FC==4:
      FONT_FILE = "Fonts/Candyinc-9Gl2.otf"
    if FC==5:
      FONT_FILE = "Fonts/ConfettiStream-A6o6.ttf"
    if FC==6:
      FONT_FILE = "Fonts/KgHappyShadows-7KqA.ttf"
    if FC==7:
      FONT_FILE = "Fonts/Lsmiserableandmagical-3jDy.otf"
    if FC==8:
      FONT_FILE = "Fonts/MarvelousScriptDemo-7lGV.otf"
    if FC==9:
      FONT_FILE = "Fonts/MyFontAddictionRegular-nEWV.ttf"
    if FC==10:
      FONT_FILE = "Fonts/NewfontRegular-8An0.ttf"
    if FC==11:
      FONT_FILE = "Fonts/Painter-LxXg.ttf"
    if FC==12:
      FONT_FILE = "Fonts/PaperSign-JRRda.ttf"
    if FC==13:
      FONT_FILE = "Fonts/Ramadhankarim-K6WD.otf"
    if FC==14:   
      FONT_FILE = "Fonts/SweetNovember-n6O1.ttf"
    if FC==15:
      FONT_FILE = "Fonts/Variety-vjZ4.ttf"

    font = ImageFont.truetype(FONT_FILE, size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(FONT_FILE, size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512-width)/2,(512-height)/2), sticktext, font=font, fill=(R, G, B))

    image_stream = io.BytesIO()
    image_stream.name = "alluka.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.client.send_file(event.chat_id, image_stream, reply_to=event.message.reply_to_msg_id)
    await event.delete()
