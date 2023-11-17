import asyncio
from aiogram import types
from data.config import ADMINS
from loader import dp, db, bot
import pandas as pd
from keyboards.inline.main import admin


@dp.message_handler(commands='admin', user_id=ADMINS)
async def get_admin_panel(message: types.Message):
    await message.answer("I remind you that you are in the Admin Panel section", reply_markup=admin)


@dp.callback_query_handler(text="all_users", user_id=ADMINS)
async def get_all_users(call: types.CallbackQuery):
    users = await db.select_all_users()
    id = []
    name = []
    for user in users:
        id.append(user[-1])
        name.append(user[1])
    data = {
        "Telegram ID": id,
        "Name": name
    }
    pd.options.display.max_rows = 10000
    df = pd.DataFrame(data)
    if len(df) > 50:
        for x in range(0, len(df), 50):
            await bot.send_message(call.message.chat.id, df[x:x + 50])
    else:
       await bot.send_message(call.message.chat.id, df)
       

@dp.callback_query_handler(text="advertising", user_id=ADMINS)
async def send_ad_to_all(call: types.CallbackQuery):
    users = await db.select_all_users()
    for user in users:
        user_id = user[-1]
        await bot.send_message(chat_id=user_id, text="@anvars_blog kanaliga obuna bo'ling")
        await asyncio.sleep(0.05)

@dp.callback_query_handler(text="clean_all_users", user_id=ADMINS)
async def get_all_users(call: types.CallbackQuery):
    await db.delete_users()
    await call.message.answer("Baza tozalandi!")
