from bot import SUPPORT_CHAT_LINK
from pyrogram import Client, filters
from bot.config import Messages as tr
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.private & filters.incoming & filters.command(['start']), group=2)
def _start(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.START_MSG.format(message.from_user.mention),
        reply_to_message_id = message.message_id
    )


@app.on_message(filters.incoming & filters.command(['help']))
def help_message(app, message):
    message.reply_text(f"Hi {message.from_user.mention()}\nI can encode Telegram files in x265, just send me a video.", quote=True)
