import os

from aiogram import Bot
from utils.models import Tickets, Lottery
from random import choice
from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def choice_winner(bot: Bot, scheduler: AsyncIOScheduler, lottery: Lottery):
    Tickets.drop_table()
    scheduler.shutdown()
    users = [i.user_id for i in Tickets.select()]
    if not users:
        lottery.winner = 0
        lottery.save()
        return await bot.send_message(os.getenv('CHANNEL_ID'), f'Победителя для вчерашнего розыгрыша нет, '
                                                               f'потому что никто не участвовал!')
    winner_id = choice(users)
    winner_user = await bot.get_chat_member(os.getenv('CHANNEL_ID'), winner_id)
    await bot.send_message(os.getenv('CHANNEL_ID'),
                           f'''Победитель вчерашнего розыгрыша @{winner_user.user.username}, поздравляем 👍

Благодарим всех за участие!''')
    lottery.winner = winner_id
    lottery.save()
