#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
from math import ceil
import asyncio
import json
import random
import re
from telethon import events, custom
from uniborg.util import admin_cmd, humanbytes


@borg.on(admin_cmd(  # pylint:disable=E0602
    pattern="ib (.[^ ]*) (.*)"
))
async def _(event):
    # https://stackoverflow.com/a/35524254/4723940
    if event.fwd_from:
        return
    bot_username = event.pattern_match.group(1)
    search_query = event.pattern_match.group(2)
    try:
        output_message = ""
        bot_results = await event.client.inline_query(  # pylint:disable=E0602
            bot_username,
            search_query
        )
        i = 0
        for result in bot_results:
            output_message += "{} {} `{}`\n\n".format(
                result.title,
                result.description,
                ".icb " + bot_username + " " + str(i + 1) + " " + search_query
            )
            i = i + 1
        await event.edit(output_message)
    except Exception as e:
        await event.edit("{} did not respond correctly, for **{}**!\n\
            `{}`".format(bot_username, search_query, str(e)))


@borg.on(admin_cmd(  # pylint:disable=E0602
    pattern="icb (.[^ ]*) (.[^ ]*) (.*)"
))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    bot_username = event.pattern_match.group(1)
    i_plus_oneth_result = event.pattern_match.group(2)
    search_query = event.pattern_match.group(3)
    try:
        bot_results = await borg.inline_query(  # pylint:disable=E0602
            bot_username,
            search_query
        )
        message = await bot_results[int(i_plus_oneth_result) - 1].click(event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True)
    except Exception as e:
        await event.edit(str(e))


# pylint:disable=E0602
if Config.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == borg.uid and query.startswith("@meanii"):
            rev_text = query[::-1]
            buttons = paginate_help(0, borg._plugins, "helpme")
            result = builder.article(
                "© @meanii",
                text="{}\nℂ𝕦𝕣𝕣𝕖𝕟𝕥𝕝𝕪 𝕃𝕠𝕒𝕕𝕖𝕕 ℙ𝕝𝕦𝕘𝕚𝕟𝕤: {}".format(
                    query, len(borg._plugins)),
                buttons=buttons,
                link_preview=True
            )
        elif query.startswith("meanii"):
            result = builder.article(
                "@meanii: Noob/xD 👨🏻‍💻",
                text=f"[meanii](https://telegra.ph/file/dff89307eb7ee61c4b9b2.mp4)",
                buttons=[],
                link_preview=True
            )
        else:
            result = builder.article(
                "© @meanii",
                text="""
**@allukabot specially customized for used SUDO and NORMAL users **
**customized by: @meanii**
**ZoldyckFamily™**  [⠀](https://telegra.ph/file/dff89307eb7ee61c4b9b2.mp4)
**Custom Built Fork:** https://github.com/mitshuhataki/kaito/""",
                buttons=[
                    [custom.Button.url("👤Contact Creator👤", "https://telegram.dog/meanii"), custom.Button.url(
                        "📼Instagram📼", "https://www.instagram.com/mitshuhataki")],
                    [custom.Button.url("👨‍💻Website👨‍💻", "https://anilchauhanxda.github.io")], [custom.Button.url(
                        "🎵lub🎵", "https://telegram.dog/songsxd/547")],
                    [custom.Button.url("🌚Youtube Channel🌚", "https://www.youtube.com/channel/UC6FsUGrV-fJtWqRykYfJscg")]
                ],
                link_preview=True
            )
        await event.answer([result] if result else None)


    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == borg.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number + 1, borg._plugins, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "⚠️ Warning: Don't Press Any Buttons ⚠️"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == borg.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                borg._plugins,  # pylint:disable=E0602
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "Please get your own Bot, and don't edit my messages!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"ub_plugin_(.*)")
    ))
    async def on_plug_in_callback_query_handler(event):
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = borg._plugins[plugin_name].__doc__[
            0:125]  # pylint:disable=E0602
        reply_pop_up_alert = help_string if help_string is not None else \
            "No DOCSTRING has been setup for {} plugin".format(plugin_name)
        reply_pop_up_alert += "\n\n Use .unload {} to remove this plugin\n\
            © @r4v4n4".format(plugin_name)
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = 2
    multi = "😇🤠🤡😈👿👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🙈🙉🙊👦👧👨👩👴👵👶"
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {} {}".format(random.choice(list(multi)), x, random.choice(list(multi))),
        data="ub_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("⏪", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("⏩", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
