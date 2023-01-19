from typing import Callable

from aiogram import F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.types import CallbackQuery

from aiocalendar import DateCalendar
from utils import DateCallback, SelectMonthCallback, SelectYearCallback


async def change_month(callback_data: SelectMonthCallback, handler: Callable):
    pass


async def change_year(callback_data: SelectYearCallback, handler: Callable):
    pass


async def select_date(callback: CallbackQuery, callback_data: DateCallback, state: FSMContext, bot: Bot):
    data = await state.storage.get_data(bot, StorageKey(bot.id, 92, 92))
    handler = data[str(callback.from_user.id)]
    await handler(callback, callback_data, state)

