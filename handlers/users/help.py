from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.constants import help_message
from loader import dp


@dp.message_handler(CommandHelp(), state="*")
async def bot_help(message: types.Message):
    await message.answer(help_message, disable_web_page_preview=True)
