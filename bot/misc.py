from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from loguru import logger

from bot.config import config

app_dir: Path = Path(__file__).parent.parent

bot = Bot(config.bot_token.get_secret_value(), parse_mode=types.ParseMode.HTML)
storage = RedisStorage2(
    host=config.redis_host, port=config.redis_port, db=config.redis_db
)
dp = Dispatcher(bot, storage=storage)


def setup():
    from bot import middlewares

    middlewares.setup(dp)

    logger.info("Configure handlers...")

    import bot.handlers
