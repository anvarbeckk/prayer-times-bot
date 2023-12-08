from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db, bot
from data.config import ADMINS
from data.constants import introduction, see_help


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    username = message.from_user.username
    user = await db.select_user(telegram_id=message.from_user.id)
    if user is None:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )
        # ADMINGA xabar beramiz
        count = await db.count_users()
        msg = f"@{user[2]} joined the base.\nthere are {count} users in the database"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    # user = await db.select_user(telegram_id=message.from_user.id)
    name = message.from_user.full_name
    if username is None:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} has already been added to the database")
        await message.answer(
            introduction)
        await message.answer(see_help)
    else:
        # await bot.send_message(chat_id=ADMINS[0], text=f"@{username} has already been added to the database")
        await message.answer(introduction)
        await message.answer(see_help)

