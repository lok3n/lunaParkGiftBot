import os
from aiogram import Bot
from aiogram.types import FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.models import Tickets, Lottery
from handlers.choice_winner import choice_winner


async def start_lottery(bot: Bot, text: str):
    Tickets.create_table()
    lottery = Lottery.create()
    kb = InlineKeyboardBuilder().button(text='Участвовать', callback_data=f'click {lottery.id}').as_markup()
    await bot.send_photo(os.getenv('CHANNEL_ID'), caption=text, photo=FSInputFile(os.getenv('PHOTO_FILENAME')),
                         reply_markup=kb)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(choice_winner, 'cron', hour=9, kwargs={'bot': bot, 'scheduler': scheduler,
                                                             'lottery': lottery})
    scheduler.start()
