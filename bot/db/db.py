from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.config import config

engine = create_async_engine(url=config.postgres_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
