from aiogram import F, Router
from aiogram.types import CallbackQuery
from utils.models import Tickets, Lottery

click_router = Router()


@click_router.callback_query(F.data.startswith('click'))
async def handle_click_btn(callback: CallbackQuery):
    lottery = Lottery.get_by_id(int(callback.data.split()[1]))
    if lottery.winner:
        return await callback.answer('❌ Лотерея неактивна')
    ticket = Tickets.get_or_none(Tickets.user_id == callback.from_user.id)
    if ticket:
        return await callback.answer('❌ Вы уже участвуете!')
    Tickets.create(user_id=callback.from_user.id)
    return await callback.answer('✅ Теперь Вы участвуете в розыгрыше!', show_alert=True)
