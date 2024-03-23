from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (Message, InlineKeyboardButton,
                           InlineKeyboardMarkup)
from tg.lexicon.lexicon import LEXICON

assistance_router: Router = Router()

url_button: InlineKeyboardButton = InlineKeyboardButton(
    text='"There is a quick and easy way" you say',
    url='https://github.com/iwantsomemarzipan/The-Smith-Bot')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button]])


# Команда для получения ссылки репозитория
@assistance_router.message(Command(commands='info'))
async def process_info_command(message: Message):
    await message.answer(LEXICON['/info'], reply_markup=keyboard)


# Помощь
@assistance_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])
