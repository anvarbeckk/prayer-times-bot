import aiohttp
import asyncpg
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.postgresql import Database
from data import config
from data.config import DB_USER, DB_PASS, DB_HOST


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
#
# session = aiohttp.ClientSession()
#
# cities = db.