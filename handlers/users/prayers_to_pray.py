from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from loader import dp, db, bot
import aioschedule
import asyncio
import datetime
import requests
from utils.prayer_time_config import days, p_api
from states.states import UserState


@dp.message_handler(state=UserState.remind_p_time)
async def remind_prayer_time(message: types.Message):
    await message.answer("Time to pray")


async def scheduler(message: types.Message):
    latitude = message.location.latitude
    longitude = message.location.longitude
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    p_url = f"{p_api}/{year}/{month}?longitude={longitude}&latitude={latitude}"
    response = requests.get(p_url)
    # print(response.content)
    h_one = response.json()
    h_two = h_one.get('data')[days]['timings']
    # print(h_two)

    today = h_one.get('data')[days]['date']['readable']
    # aioschedule.every().day.at("17:00").do(remind_prayer_time)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
