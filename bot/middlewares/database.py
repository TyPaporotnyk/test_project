from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from bot.db.db import async_session_maker


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    @staticmethod
    async def add_db_session(data: dict):
        async with async_session_maker() as session:
            data["db_session"] = session

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.add_db_session(data)

    async def on_pre_process_callback_query(
        self, query: types.CallbackQuery, data: dict
    ):
        await self.add_db_session(data)
