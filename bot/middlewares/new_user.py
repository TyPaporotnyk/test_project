from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User


class NewUserMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def on_pre_process_message(self, message: types.Message, data: dict):
        db_session: AsyncSession = data.get("db_session")
        t_user = message.from_user

        stmt = select(User).filter_by(id=t_user.id)
        user = await db_session.execute(stmt)
        user = user.scalar_one_or_none()
        if user is None:
            new_user = User(
                id=t_user.id,
                username=t_user.username,
                first_name=t_user.first_name,
                last_name=t_user.last_name,
                language_code=t_user.language_code,
                is_bot=t_user.is_bot,
            )
            db_session.add(new_user)
            await db_session.commit()
            logger.debug("Added new user {user}", user=message.from_user.id)
