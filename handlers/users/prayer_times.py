import requests
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from loader import dp, db, bot
import datetime
from utils.prayer_time_config import days, p_api
from states.states import UserState


@dp.message_handler(commands='prayer_times', state="*")
async def prayer_times(message: types.Message):
    location_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    location_markup.add(types.KeyboardButton("Location", request_location=True))
    await message.answer("<b>Please, send your location</b>", reply_markup=location_markup)
    await UserState.get_city.set()


@dp.message_handler(state=UserState.get_city, content_types=['location'])
async def get_city_name(message: types.Message):
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
    # print(today)

    p_result = f"<b>{h_one.get('data')[days]['date']['hijri']['day']} {h_one.get('data')[days]['date']['hijri']['month']['en']} {h_one.get('data')[days]['date']['hijri']['year']} {h_one.get('data')[days]['date']['hijri']['designation']['abbreviated']}</b>\n\nHere are your prayer times for today:\n\n<code>Fajr:     {h_two['Fajr'][0:5]}\nDhuhr:    {h_two['Dhuhr'][0:5]}\nAsr:      {h_two['Asr'][0:5]}\nMaghrib:  {h_two['Maghrib'][0:5]}\nIsha:     {h_two['Isha'][0:5]}</code>"

    await message.answer(str(p_result), reply_markup=ReplyKeyboardRemove())
