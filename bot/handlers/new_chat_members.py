from aiogram import types
from loguru import logger

from bot.misc import dp


@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_chat_member(message: types.Message):
    logger.info(
        "User {user} is a new chat {chat} member",
        user=message.from_user.id,
        chat=message.chat.id,
    )
    await message.answer(
        f"Hello, {message.from_user.full_name}\n" f"Welcome to our cozy lair.\n"
    )


@dp.message_handler(content_types=types.ContentTypes.LEFT_CHAT_MEMBER)
async def left_chat_member(message: types.Message):
    logger.info(
        "User {user} has been left from the chat {chat}",
        user=message.from_user.id,
        chat=message.chat.id,
    )
