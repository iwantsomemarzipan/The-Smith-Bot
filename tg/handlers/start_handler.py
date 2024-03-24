from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from tg.lexicon.lexicon import LEXICON

start_router: Router = Router()


# Start command
@start_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON['/start'])
