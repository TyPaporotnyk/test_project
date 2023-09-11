from aiogram import types
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import hlink
from loguru import logger

from bot.misc import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    logger.info("User {user} start conversation with bot", user=message.from_user.id)

    await message.answer(
        f"Hello, {message.from_user.full_name}\n"
        f"This is a test bot to test my knowledge of aiogram.\n"
    )


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    logger.info(
        "User {user} read help in {chat}",
        user=message.from_user.id,
        chat=message.chat.id,
    )
    await message.answer(
        f"This bot is using polling instead webhooks.\n"
        f"Also he is using default logging middlewares.\n"
        f"Source code of this project at {hlink('GitHub', 'https://github.com/TyPaporotnyk/test-project')}"
    )
