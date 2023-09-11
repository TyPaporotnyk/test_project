from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loguru import logger

from bot.db.db import async_session_maker


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    @staticmethod
    async def add_db_session(data: dict):
        async with async_session_maker() as session:
            data["db_session"] = session

    @staticmethod
    async def close_db_session(data: dict):
        db_session = data.get("db_session")

        if db_session is not None:
            logger.debug("Closing database session...")
            await db_session.close()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.add_db_session(data)

    async def on_post_process_update(self, message: types.Message, results, data: dict):
        await self.close_db_session(data)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.add_db_session(data)

    async def on_post_process_callback_query(self, callback_query: types.CallbackQuery, results, data: dict):
        await self.close_db_session(data)
