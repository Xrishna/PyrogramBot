from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Its Just A Pyrogram Test Bot Of @Itsxrishna",
        reply_to_message_id=update.message_id
    )
    
