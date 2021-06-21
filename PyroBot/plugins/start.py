from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Its Just A Pyrogram Test Bot Of @Itsxrishna",
        reply_to_message_id=update.message_id
    )

    @Client.on_message(filters.command(["rate"]))
async def start(bot, update):
    await bot.forward_messages(
    chat_id=update.chat.id,
    from_chat_id=-1001159467641,
    message_ids=3
)
