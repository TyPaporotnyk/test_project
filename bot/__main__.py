import asyncio

from bot import misc
from bot.misc import dp
from bot.utils import logging


async def main():
    logging.setup()
    misc.setup()

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
