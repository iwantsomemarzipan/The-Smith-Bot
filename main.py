import asyncio
import logging

from config_reader import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.session.aiohttp import AiohttpSession
from tg.handlers.start_handler import start_router
from tg.handlers.generation_handler import generation_router
from tg.handlers.user_assistance_handler import assistance_router

logging.basicConfig(level=logging.INFO)

session: AiohttpSession = AiohttpSession(proxy='http://proxy.server:3128')
storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot(token=config.bot_token.get_secret_value(), session=session)
dp: Dispatcher = Dispatcher()

dp.include_router(start_router)
dp.include_router(generation_router)
dp.include_router(assistance_router)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
