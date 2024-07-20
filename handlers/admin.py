import os

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from handlers.send_message import start_lottery
from utils.models import Settings


admin_router = Router()


@admin_router.message(Command('start_new_lottery'))
async def start_new_lottery(message: Message):
    if str(message.from_user.id) in os.getenv('ADMINS').split(','):
        settings = Settings.get()
        await start_lottery(message.bot, settings.text)
        await message.answer('✅ Успешно!')


@admin_router.message(Command('edit_text'))
async def edit_text(message: Message):
    if str(message.from_user.id) in os.getenv('ADMINS').split(','):
        settings = Settings.get()
        new_text = message.text.split()
        if len(new_text) == 1:
            return await message.answer('❌ Введите комманду в формате: /edit_text *новый текст*',
                                        parse_mode='HTML')
        settings.text = ' '.join(new_text[1:])
        settings.save()
        await message.answer('✅ Успешно!')
        await message.answer(settings.text)

