from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (Message, InlineKeyboardButton,
                           InlineKeyboardMarkup)
from tg.lexicon.lexicon import LEXICON

assistance_router: Router = Router()

url_button: InlineKeyboardButton = InlineKeyboardButton(
    text='"There is a quick and easy way" you say',
    url='https://private-spruce-237.notion.site/7364ad0de7de4a279856a17f687b9da8?pvs=4')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button]])


# Команда для получения ссылки на страницу в ноушен
@assistance_router.message(Command(commands='info'))
async def process_info_command(message: Message):
    await message.answer(LEXICON['/info'], reply_markup=keyboard)


# Помощь
@assistance_router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])
