from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
import asyncio
import os
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.click import click_router
from handlers.send_message import start_lottery
from handlers.admin import admin_router
from utils.models import Lottery, Settings


load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()
dp.include_routers(click_router, admin_router)


async def main():
    Lottery.create_table()
    Settings.create_table()
    Settings.get_or_create()

    scheduler = AsyncIOScheduler()
    settings = Settings.get()
    scheduler.add_job(start_lottery, 'cron', hour=10, kwargs={'bot': bot, 'text': settings.text})
    scheduler.start()
    print('started')
    await bot.set_my_description(f'ℹ Привет! Я бот-помощник для проведения розыгрышей')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
