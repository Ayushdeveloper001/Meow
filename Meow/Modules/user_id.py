from pyrogram import Client, filters
from pyrogram.types import Message

from Meow.Modules.helpers.get_file_id import get_file_id
from Meow import HNDLR, LOGS_CHANNEL, SUDO_USERS, app


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["id"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["id"], prefixes=HNDLR))
async def showid(_, message: Message):
    chat_type = message.chat.type

    if chat_type == "private":
        user_id = message.chat.id
        await message.reply_text(f"<code>{user_id}</code>")

    elif chat_type in ["group", "supergroup"]:
        _id = ""
        _id += "<b>ID group</b>: " f"<code>{message.chat.id}</code>\n"
        if message.reply_to_message:
            _id += (
                "<b> User ID </b>: "
                f"<code>{message.reply_to_message.from_user.id}</code>\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "<b>ID pengguna</b>: " f"<code>{message.from_user.id}</code>\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
