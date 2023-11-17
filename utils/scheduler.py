import asyncio
import aioschedule

from loader import db


def congratulation_birth_day():
    pass


async def scheduler():

    aioschedule.every().day.at("12:00").do(congratulation_birth_day)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
