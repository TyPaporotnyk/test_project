from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

from .database import DatabaseMiddleware
from .new_user import NewUserMiddleware


def setup(dispatcher: Dispatcher):
    logger.info("Configure middlewares...")

    # Your middlewares setup here
    dispatcher.middleware.setup(LoggingMiddleware("bot"))
    dispatcher.middleware.setup(DatabaseMiddleware())
    dispatcher.middleware.setup(NewUserMiddleware())
