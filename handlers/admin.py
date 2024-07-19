import os

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from handlers.send_message import start_lottery
from template_message import MESSAGE

admin_router = Router()


@admin_router.message(Command('start_new_lottery'))
async def start_new_lottery(message: Message):
    if str(message.from_user.id) in os.getenv('ADMINS').split(';'):
        await start_lottery(message.bot, MESSAGE)
        await message.answer('Completed!')

